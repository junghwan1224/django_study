from django.contrib import admin
from .models import Post
from .models import MainTheme
from .models import MidTheme
from .models import SubTheme

from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


# class SummerAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content',)

admin.site.register(MainTheme)
admin.site.register(MidTheme)
admin.site.register(SubTheme)
admin.site.register(Post, SummernoteModelAdmin)
