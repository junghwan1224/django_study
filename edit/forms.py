from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Article


class ArticleForm(forms.ModelForm):

    content = forms.CharField(widget=SummernoteWidget(), label='')

    class Meta:
        model = Article
        # widgets = {
        #     'title': SummernoteWidget(),
        #     'content': SummernoteInplaceWidget(),
        # }
        fields = '__all__'
