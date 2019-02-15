from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post


class PostForm(forms.ModelForm):

    content = forms.CharField(widget=SummernoteWidget(), label='')

    class Meta:
        model = Post
        exclude = ('author', 'created_at', 'updated_at', 'apply_user',)
