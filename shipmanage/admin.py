from django.contrib import admin
from .models import Ship, Berth, Order
# Register your models here.

admin.site.site_header = '港口物流信息系统'
admin.site.site_title = 'PLIS管理员界面'

@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):

    list_display = ("ship_name", "ship_capacity", "is_anchored", )

@admin.register(Berth)
class BerthAdmin(admin.ModelAdmin):

    list_display = ("berth_name", "berth_cap", "berth_used", )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ("order_id", "goods_name", "goods_amount", "unit", "order_status", )