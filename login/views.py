from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LoginForm

# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user = login_form.cleaned_data['user']
                login(request, user)
                return redirect('/')
        else:
            login_form = LoginForm()

        context = {'login_form':login_form, }
        return render(request, "login.html", context)

def home_page(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return redirect('login/')