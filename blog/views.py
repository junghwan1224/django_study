from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse

from blog.models import Post
from blog.forms import PostForm
from django.utils import timezone

from edit.forms import ArticleForm
from edit.models import Article

from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.


# post list 를 published date 의 역순으로 정렬
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/blog_list.html', {'posts': posts})


class PostList(View):

    def get(self, request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, 'blog/blog_list.html', {'posts': posts})


class PostTemplate(TemplateView):
    template_name = 'blog/blog_list.html'

    def get_context_data(self, **kwargs):
        context = super(PostTemplate, self).get_context_data(**kwargs)
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        context['posts'] = posts
        return context


class PostListView(ListView):

    model = Post
    template_name = 'blog/blog_list_view.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):

    model = Post
    template_name = 'blog/blog_detail_view.html'
    context_object_name = 'post'


# 글 내용
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/blog_detail.html', context)


# 글쓰기
def post_create(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            newForm = Post.objects.create(
                    author=request.user,
                    title=form.cleaned_data['title'],
                    text=form.cleaned_data['text'],
                    published_date=timezone.now(),
                )
            newForm.save()

            # newForm = form.save(commit=False)
            # newForm.author = request.user
            # newForm.publish()
            # newForm.save()

            url = reverse('blog:post_detail', kwargs={'pk': newForm.pk})
            return redirect(url)
        else:
            print('form validation error')
            print(form.errors)

    else:
        form = PostForm()
        context = {
            'form': form,
        }
        return render(request, 'blog/blog_create.html', context)


# 글 수정
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.publish()
            newForm.save()

            url = reverse('blog:post_detail', kwargs={'pk': newForm.pk})
            return redirect(url)

    else:
        form = PostForm(instance=post)
        context = {
            'form': form,
        }
        return render(request, 'blog/blog_edit.html', context)


# summernote test
def post_edit_summer(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # print(form)
            form.save()
            return redirect(reverse('blog:post_list'))

    form = ArticleForm()
    ctx = {
        'form': form
    }
    return render(request, 'blog/blog_summer.html', ctx)


def summer_content(request, pk):
    article = get_object_or_404(Article, pk=pk)
    ctx = {
        'article': article
    }
    return render(request, 'blog/detail.html', ctx)
