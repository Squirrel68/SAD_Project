from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Customer

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Đăng ký thành công!")
            return redirect("customer:profile")
    else:
        form = RegisterForm()
    return render(request, "customer/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Đăng nhập thành công!")
            return redirect("customer:profile")
        else:
            messages.error(request, "Sai thông tin đăng nhập!")
    return render(request, "customer/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Đăng xuất thành công!")
    return redirect("customer:login")

@login_required
def profile_view(request):
    customer = Customer.objects.get(user=request.user)
    return render(request, "customer/profile.html", {"user": request.user, "customer": customer})
