from django import forms
from blog.models import Post

# from django_summernote import fields as summer_fields


class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(
            attrs={
                'placeholder': 'Input Title',
            }
        ))

    text = forms.CharField(widget=forms.Textarea(
            attrs={
                'placeholder': 'Input Content',
            }
        ))

    class Meta:
        model = Post
        exclude = ('author', 'created_date', 'published_date', )

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if ('title' in title):
            return title
        else:
            raise forms.ValidationError('incorrect title')

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if(text is not None):
            return text
        else:
            raise forms.ValidationError('incorrect text')


# class SummerForm(forms.ModelForm):
#     fields = summer_fields.SummernoteTextFormField()

#     class Meta:
#         model = SummerNote
#         fields = ('fields',)
