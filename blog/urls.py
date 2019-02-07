from django.urls import path
from . import views
from .views import PostList
from .views import PostTemplate
from .views import PostListView
from .views import PostDetailView

app_name = 'blog'


urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/new', views.post_create, name='post_create'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/', views.post_edit_summer, name='post_edit_summer'),
    path('content/<int:pk>', views.summer_content, name='summer_content'),

    path('post_tem/', PostTemplate.as_view(), name='post_template'),
    path('post_list_view/', PostListView.as_view(), name='post_list_view'),
    path('post_detail_view/<int:pk>', PostDetailView.as_view(), name='post_detail_view'),
]
