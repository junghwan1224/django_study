from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# from django_summernote import models as summer_model
# from django_summernote import fields as summer_fields

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True
        )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absoulte_url(self):
        pass

    def __str__(self):
        return self.title
