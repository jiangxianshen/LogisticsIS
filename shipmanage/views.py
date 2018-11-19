from django.shortcuts import render

# Create your views here.

def ship_manage(request):
    return render(request, "ship.html")


def order_manage(request):
    return render(request, "order.html")