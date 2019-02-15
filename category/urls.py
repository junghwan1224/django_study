from django.urls import path
from . import views

app_name = 'category'


urlpatterns = [
    path('list/', views.category_list, name='category_list'),

    path('<int:pk>/post/', views.post_create, name='post_create'),
    path('all/list/<int:theme_pk>/', views.AllList.as_view(), name='all_list'),
    path('buy/list/<int:theme_pk>/', views.BuyList.as_view(), name='buy_list'),
    path('sell/list/<int:theme_pk>/', views.SellList.as_view(), name='sell_list'),
    path('list/<int:pk>/', views.post_detail, name='post_detail'),
    path('apply/<int:pk>', views.apply_post, name='apply_post'),
]
