from django.db import models
import time
import random

def orderid_generate():
    '''
    自动按照时间生成订单号，末四位为随机码
    '''
    clock = time.localtime(time.time())
    return '%04.0f%02.0f%02.0f%02.0f%02.0f%02.0f%04.0f' % (clock.tm_year,
                                                     clock.tm_mon,
                                                     clock.tm_mday,
                                                     clock.tm_hour,
                                                     clock.tm_min,
                                                     clock.tm_sec,
                                                     random.randint(0, 9999))

# Create your models here.
class Ship(models.Model):
    ship_id = models.IntegerField(primary_key=True)
    ship_name = models.CharField(max_length=50)
    is_anchored = models.BooleanField(default=True)
    ship_manager = models.CharField(max_length=20)
    ship_capacity = models.IntegerField(default=15)
    ship_owner = models.CharField(max_length=50,default="PLIS")
    url_height = models.PositiveIntegerField(default=75)
    url_width = models.PositiveIntegerField(default=75)
    ship_photo = models.ImageField(upload_to="icons", height_field='url_height', width_field='url_width')

    def __str__(self):
        return "%s" % (self.ship_name)


class Berth(models.Model):
    berth_name = models.CharField(max_length=50)
    berth_id = models.IntegerField(primary_key=True)
    berth_cap = models.IntegerField(editable=False, default=20)
    berth_used = models.IntegerField()

    def __str__(self):
        return "%s" % (self.berth_name)

class Order(models.Model):
    order_id = models.CharField(primary_key=True, default=orderid_generate(), max_length=18, editable=False)
    goods_name = models.CharField(max_length=50)
    cargo_owner = models.CharField(max_length=50, default=" ")
    goods_amount = models.IntegerField()
    unit = models.CharField(max_length=10, default="KG", choices=(("KG","kilogram"),
                                                                  ("T","Ton"),
                                                                  ))
    create_time = models.DateTimeField(auto_now_add=True, editable=False)
    target_port = models.CharField(max_length=50, default=" ")
    arrive_time = models.DateTimeField(blank=True, null=True)
    ship_use = models.ForeignKey(Ship, on_delete=models.DO_NOTHING)
    manager = models.CharField(max_length=50, default=" ")
    order_status = models.BooleanField(default=False) #False表示订单未完成

    def __str__(self):
        return "%s" % (self.order_id)


