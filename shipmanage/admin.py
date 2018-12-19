from django.contrib import admin
from .models import Ship, Berth, Order
# Register your models here.


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):

    list_display = ("ship_name", )

@admin.register(Berth)
class BerthAdmin(admin.ModelAdmin):

    list_display = ("berth_name", )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ("order_id", "goods_name", "goods_amount", "unit", "order_status", )