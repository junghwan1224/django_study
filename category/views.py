from django.shortcuts import render, reverse, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import MainTheme
from .models import Post
from accounts.models import Account
from .forms import PostForm
# Create your views here.


def category_list(request):
    main = get_object_or_404(MainTheme, pk=1)
    print(main)
    print(main.related_mid_theme.all())
    ctx = {
        'mainTheme': main,
    }
    return render(request, 'c_list.html', ctx)


def buy_post_list(request):
    post = Post.objects.filter(post_type='Buy')


def sell_post_list(request):
    post = Post.objects.filter(post_type='Sell')


def post_detail(request, pk):
    pass


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            account = Account.objects.get(user_id=request.user.pk)
            saveForm = form.save(commit=False)
            saveForm.author = account
            saveForm.save()
            return redirect(reverse('blog:post_list_view'))

    form = PostForm()
    ctx = {
        'form': form
    }
    return render(request, 'post_create.html', ctx)
