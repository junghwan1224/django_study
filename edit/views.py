from django.shortcuts import render
from .forms import ArticleForm

# Create your views here.


def post_edit(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            pass

    form = ArticleForm()
    ctx = {
        'form': form
    }
    return render(request, 'post/post.html', ctx)
