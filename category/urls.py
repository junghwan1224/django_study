from django.urls import path
from . import views

app_name = 'category'


urlpatterns = [
    path('list/', views.category_list, name='category_list'),
    path('post/', views.post_create, name='post_create'),
]
