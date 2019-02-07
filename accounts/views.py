from django.shortcuts import render
from django.shortcuts import redirect
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.http import Http404
from django.contrib.auth.hashers import make_password

from .forms import AccountForm
from .forms import UserForm
from .forms import LoginForm
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

    if request.method == 'POST':
        userForm = UserForm(request.POST)
        accountForm = AccountForm(request.POST)

        if userForm.is_valid() and accountForm.is_valid():
            userFormSave = userForm.save(commit=False)
            userFormSave.password = make_password(userFormSave.password)
            userFormSave.save()

            account = accountForm.save(commit=False)
            account.user = userFormSave
            account.save()

            return redirect('accounts:loginView')

    userForm = UserForm()
    accountForm = AccountForm()

    ctx = {
        'accountForm': accountForm,
        'userForm': userForm,
    }

    return render(request, 'account/signup_template.html', ctx)


def loginView(request):

    # if request.method == 'POST' and LoginForm(request.POST).is_valid():
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(username, password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            raise Http404('login failed')

    loginForm = LoginForm()
    return render(request, 'account/login_template.html', {'loginForm': loginForm})


def logoutView(request):
    logout(request)
    return redirect('accounts:loginView')
