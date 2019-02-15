from django.shortcuts import render, reverse, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.views.generic.list import ListView

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


class AllList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        theme_pk = self.kwargs['theme_pk']
        return Post.objects.filter(sub_theme__pk=theme_pk)


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
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


# 여기에도 pk 파라미터를 줘야 하는가?
@login_required
def post_create(request, pk):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            account = Account.objects.get(user_id=request.user.pk)
            saveForm = form.save(commit=False)
            saveForm.author = account
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
