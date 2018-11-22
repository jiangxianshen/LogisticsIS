from django.shortcuts import render

# Create your views here.

def ship_manage(request):
    return render(request, "shipmanage.html")


def order_manage(request):
    return render(request, "ordermanage.html")