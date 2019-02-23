from django.shortcuts import render, reverse, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

from django.views.generic.list import ListView

from .models import MainTheme
from .models import Post
from accounts.models import Account
from .forms import PostForm
from .forms import CommentForm
# Create your views here.


def category_list(request):
    main = get_object_or_404(MainTheme, pk=1)
    print(main)
    print(main.related_mid_theme.all())
    ctx = {
        'mainTheme': main,
    }
    return render(request, 'c_list.html', ctx)


class AllList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        theme_pk = self.kwargs['theme_pk']
        post = Post.objects.filter(sub_theme__pk=theme_pk)
        return post


class BuyList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        theme_pk = self.kwargs['theme_pk']
        return Post.objects.filter(sub_theme__pk=theme_pk).filter(post_type='Buy')


class SellList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        theme_pk = self.kwargs['theme_pk']
        return Post.objects.filter(sub_theme__pk=theme_pk).filter(post_type='Sell')


@login_required
def post_detail(request, pk):
    form = CommentForm(request.POST or None)
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        if form.is_valid():
            saveForm = form.save(commit=False)
            saveForm.author = request.user
            saveForm.post = post
            saveForm.save()

            return redirect(reverse(
                    'category:post_detail',
                    kwargs={'pk': pk}
                ))

    ctx = {
        'post': post,
        'commentForm': form,
    }
    return render(request, 'post_detail.html', ctx)


@login_required
def post_create(request, pk):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            account = Account.objects.get(user_id=request.user.pk)
            saveForm = form.save(commit=False)
            saveForm.author = account
            if request.FILES:
                saveForm.thumbnail = request.FILES['thumbnail']
            saveForm.save()
            return redirect(reverse(
                    'category:all_list',
                    kwargs={'theme_pk': pk}
                ))

    form = PostForm(initial={'sub_theme': pk})
    ctx = {
        'form': form
    }
    return render(request, 'post_create.html', ctx)


@login_required
def apply_post(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        if post.apply_user.filter(pk=request.user.pk).exists():
            print('이미 신청')
            return redirect(reverse(
                    'category:post_detail',
                    kwargs={'pk': pk}
                ))
        else:
            post.apply_user.add(request.user)
            return redirect(reverse(
                    'category:post_detail',
                    kwargs={'pk': pk}
                ))


@login_required
def apply_send_mail(request, post_pk, user_pk):
    # post = get_object_or_404(Post, pk=post_pk)
    user = get_object_or_404(User, pk=user_pk)
    url = '{0}{1}'.format(
            'http://localhost:8000',
            reverse(
                    'category:check_apply',
                    kwargs={"pk": post_pk},
                )
        )
    html = '<a href="{0}">거래하기</a>'.format(url)
    send_mail(
            '거래 매치 메일',
            '',
            settings.EMAIL_HOST_USER,
            [user.email],
            html_message=html
        )

    return redirect(reverse(
            'accounts:profileView'
        ))


@login_required
def check_apply(request, pk):
    post = get_object_or_404(Post, pk=pk)

    ctx = {
        'post': post,
    }
    return render(request, 'check_apply.html', ctx)

"""
신청했으면 거래신청 버튼 없애고 취소하던가 아니면 버튼 클릭 시 이미 신청 했다고 표시하던가
거래완료
"""
