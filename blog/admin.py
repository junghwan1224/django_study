from django.contrib import admin
from blog.models import Post
from edit.models import Article
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Article, SummernoteModelAdmin)

admin.site.register(Post)
