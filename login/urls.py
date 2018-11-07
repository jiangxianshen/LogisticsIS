from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('', views.home_page, name="homepage"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.user_register, name="register"),
    path('forget/', views.forget_password, name="forget"),
]
