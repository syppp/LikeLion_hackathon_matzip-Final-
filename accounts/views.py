from django.shortcuts import render

def home(request): 
    return render(request, 'home.html')

def register(request): 
    return render(request, 'register.html')

def login(request): 
    return render(request, 'login.html')

def input(request): 
    return render(request, 'input.html')