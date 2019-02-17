from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.http import Http404
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from .models import Account
from .forms import AccountForm
from .forms import UserForm
from .forms import LoginForm
from .forms import SignUpForm
from .forms import SignInForm

from category.models import Post
# Create your views here.


def indexView(request):
    providers = []

    for provider in get_providers():
        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    return render(request, 'allauthTemplates/index.html', {
        'providers': providers,
    })


def signupView(request):

    signupForm = SignUpForm(request.POST or None)

    if request.method == 'POST':
        if signupForm.is_valid():

            form = signupForm.save()

            address = request.POST.get('address')
            phone = request.POST.get('phone')

            Account.objects.create(
                user_id=form.id,
                address=address,
                phone=phone
                )

            return redirect('accounts:loginView')

    # userForm = UserForm()
    # accountForm = AccountForm()

    ctx = {
        'signupForm': signupForm,
    }

    return render(request, 'account/signup_template.html', ctx)


def loginView(request):

    # loginForm = SignInForm(request, request.POST or None)

    # if request.method == 'POST' and LoginForm(request.POST).is_valid():
    if request.method == 'POST':
        loginForm = SignInForm(request=request, data=request.POST)
        if loginForm.is_valid():

            user = loginForm.get_user()
            print(user)

            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

            # if user is not None:
            #     login(request, user)
            #     return redirect(settings.LOGIN_REDIRECT_URL)
            # else:
            #     raise Http404('login failed')

    loginForm = SignInForm()
    return render(request, 'account/login_template.html', {'loginForm': loginForm})


def logoutView(request):
    logout(request)
    return redirect('accounts:loginView')


@login_required
def profileView(request):
    post = Post.objects.filter(author__user=request.user)

    ctx = {
        'posts': post,
    }
    return render(request, 'account/profile_template.html', ctx)
