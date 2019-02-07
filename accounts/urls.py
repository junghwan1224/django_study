from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('', views.indexView, name='indexView'),
    path('signup/', views.signupView, name='signupView'),
    path('signin/', views.loginView, name='loginView'),
    path('signout/', views.logoutView, name='logoutView'),
]
