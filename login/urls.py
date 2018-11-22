from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('', views.home_page, name="homepage"),
    path('logout/', views.user_logout, name="logout"),
    path('forget/', views.forget_password, name="forget"),
    path('profile/', views.user_profile, name="profile"),
    path('change_email/', views.change_email, name="change_email")
]
