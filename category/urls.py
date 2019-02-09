from django.urls import path
from . import views

app_name = 'category'


urlpatterns = [
    path('list/', views.category_list, name='category_list'),

    path('post/', views.post_create, name='post_create'),
    path('all/list', views.AllList.as_view(), name='all_list'),
    path('buy/list/', views.BuyList.as_view(), name='buy_list'),
    path('sell/list/', views.SellList.as_view(), name='sell_list'),
    path('list/<int:pk>', views.post_detail, name='post_detail'),
]
