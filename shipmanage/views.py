from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from django.utils import timezone
from .models import Order
# Create your views here.

def ship_manage(request):
    return render(request, "shipmanage.html")


def order_manage(request):
    return render(request, "ordermanage.html")


def order_detail(request, order_id):
    if request.user.is_authenticated:
        if request.POST:
            order = get_object_or_404(Order, order_id=order_id)
            order.order_status = True
            order.arrive_time = timezone.now()
            order.save()
        else:
            order = get_object_or_404(Order, order_id=order_id)
        content = {"order": order}
        return render(request, "order_detail.html", content)
    else:
        return redirect('login')


def ship_detail(request, ship_id):
    pass

def order_create(request):
    pass

def search_order(request):
    pass
