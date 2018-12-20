from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from django.utils import timezone
from .models import Order, Ship
from .forms import OrderForm
# Create your views here.

def ship_manage(request):
    if request.user.is_authenticated:
        return render(request, "shipmanage.html")
    else:
        return redirect('login')


def order_manage(request):
    if request.user.is_authenticated:
        return render(request, "ordermanage.html")
    else:
        return redirect('login')


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
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')

def order_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Order_form = OrderForm(request.POST, user=request.user)
            if Order_form.is_valid():
                user = request.user
                goods_name = Order_form.cleaned_data['goods_name']
                cargo_owner = Order_form.cleaned_data['cargo_owner']
                goods_amount = Order_form.cleaned_data['goods_amount']
                unit = Order_form.cleaned_data['unit']
                target_port = Order_form.cleaned_data['target_port']
                ship_name = Order_form.cleaned_data['ship_use']
                ship_use = Ship.objects.get(ship_name=ship_name)
                manager = user.username
                new_order = Order.objects.create(goods_name=goods_name,
                                                cargo_owner=cargo_owner,
                                                goods_amount=goods_amount,
                                                unit=unit,
                                                target_port=target_port,
                                                ship_use=ship_use,
                                                manager=manager)
                message = new_order.order_id
                context = {'Order_form': Order_form, 'message': message}
                return render(request, "order_create.html", context)
        else:
            Order_form = OrderForm()
            context = {'Order_form': Order_form,}
            return render(request, "order_create.html", context)
    else:
        return redirect('login')

def search_order(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')