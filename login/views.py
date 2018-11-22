from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout
from .forms import LoginForm, ProfileForm
from .models import ManagerUser

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
        return redirect('login')

def user_logout(request):
    logout(request)
    return redirect(request.GET.get('from', reverse('login')))

def forget_password(request):
    return render(request, "forgot.html")

def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            Profile_form = ProfileForm(request.POST, user=request.user)
            if Profile_form.is_valid():
                user = request.user
                new_pass = Profile_form.cleaned_data['new_password']
                user.set_password(new_pass)
                user.save()
                logout(request)
                return redirect('login')
        else:
            Profile_form = ProfileForm()

        context = {'Profile_form': Profile_form, }
        return render(request, "profiles.html", context)

def change_email(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            user = request.user
            user.email = email
            user.save()
        return render(request,"change_email.html")