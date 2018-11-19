from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order_manage, name="order"),
    path('ships/', views.ship_manage, name="ships"),
]
