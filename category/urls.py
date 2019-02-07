from django.urls import path
from . import views

app_name = 'category'


urlpatterns = [
    path('list/', views.category_list, name='category_list'),
    path('sell_post/<int:pk>', views.sell_post, name='sell_post'),
    path('purchase_post/<int:pk>', views.purchase_post, name='purchase_post'),
]
