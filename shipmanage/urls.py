from django.urls import path
from . import views

urlpatterns = [
    path('order/page=<int:num>', views.order_manage, name="order"),
    path('ships/page=<int:num>', views.ship_manage, name="ships"),
    path('search?=<search>', views.search_order, name="search_order"),
    path('order/id=<int:order_id>', views.order_detail, name="order_detail"),
    path('order/new_order', views.order_create, name="new_order"),
    path('ships/id=<int:ship_id>', views.ship_detail, name="ship_detail"),
]
