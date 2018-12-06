from django.db import models

# Create your models here.
class Ship(models.Model):
    ship_id = models.IntegerField(primary_key=True)
    ship_name = models.CharField(max_length=50)
    is_anchored = models.BooleanField(default=True)
    ship_manager = models.CharField(max_length=20)

    def __str__(self):
        return "%s" % (self.ship_name)


class Berth(models.Model):
    berth_name = models.CharField(max_length=50)
    berth_id = models.IntegerField(primary_key=True)
    berth_cap = models.IntegerField(editable=False, default=20)
    berth_used = models.IntegerField(max_length=20)

    def __str__(self):
        return "%s" % (self.berth_name)

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    goods_name = models.CharField(max_length=50)
    goods_amount = models.IntegerField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    arrive_time = models.DateTimeField()
    ship_use = models.ForeignKey(Ship, on_delete=models.DO_NOTHING)
    order_status = models.BooleanField(default=False) #False表示订单未完成

    def __str__(self):
        return "%s" % (self.order_id)