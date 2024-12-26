from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistraionForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == "POST":
        register_form = UserRegistraionForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "New User Created Successfully. Please login ")
            return redirect('login')
    else:
        register_form = UserRegistraionForm()
        
        
    context = {
        'current_page': 'register',
        'register_form': register_form,
        'title' : 'register'
    }
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                messages.success(request, "User Loggedin Successfully")
                return redirect('index')
            else:
                messages.success(request, "username/password is Incorrect. Please try again.")
                return redirect('login')
            
    else:
        form = UserLoginForm()
    
    context = {
                'title': "Login Page",
                'form' : form,
                'current_page': 'login'
            } 
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, "User Logged out successfully")
    return redirect('index')