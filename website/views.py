from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['username']  # Use the actual field name
        password = request.POST['password']  # Use the actual field name

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('home')
        else:
            messages.error(request, "Authentication failed. Please check your credentials.")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)  # Log the user out
    messages.success(request, "You have been logged out.")
    return redirect('home')
def register_user(request):
    return  render(request, 'register.html', {})
