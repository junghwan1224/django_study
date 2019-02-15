from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post
from .models import Comment


class PostForm(forms.ModelForm):

    content = forms.CharField(widget=SummernoteWidget(), label='')

    class Meta:
        model = Post
        exclude = ('author', 'post_status', 'created_at', 'updated_at', 'apply_user',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('author', 'created_at', 'post',)
