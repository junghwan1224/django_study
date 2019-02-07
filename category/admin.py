from django.contrib import admin
from .models import SellPost, PurchasePost
# Register your models here.

admin.site.register(SellPost)
admin.site.register(PurchasePost)
