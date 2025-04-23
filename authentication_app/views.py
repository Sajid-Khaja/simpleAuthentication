from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Register View
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("user_login") 
    else:
        form = RegisterForm()
    return render(request, "authentication_app/register.html", {"form": form})

# Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  
        else:
            return render(request, "authentication_app/login.html", {"error": "Invalid credentials"})

    return render(request, "authentication_app/login.html") 

# Logout View
def user_logout(request):
    logout(request)
    return redirect("user_login")  


@login_required(login_url='user_login') 
def dashboard(request):
    return render(request, "authentication_app/dashboard.html", {"username": request.user.username})
