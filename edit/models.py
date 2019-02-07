from django.db import models

# from django_summernote import models as summer_model
# from django_summernote import fields as summer_fields

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50, default='')
    content = models.TextField(default='')

    def __str__(self):
        return self.title
