from django.shortcuts import render, redirect
from .models import Register, RegisterManager
from django.contrib import messages

def login(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'success.html')