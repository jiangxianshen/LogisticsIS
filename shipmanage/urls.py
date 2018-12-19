from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order_manage, name="order"),
    path('ships/', views.ship_manage, name="ships"),
    path('search?=<search>', views.search_order, name="search_order"),
    path('order/id=<int:order_id>', views.order_detail, name="order_detail")
]
