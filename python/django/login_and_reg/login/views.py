from django.shortcuts import render, redirect
from .models import Register, RegisterManager
from django.contrib import messages
from django.core.exceptions import ValidationError
import bcrypt




def home(request):
    return render(request, 'index.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def login(request):
    if request.method == "GET":
        return redirect('/')
    login_errors = Register.objects.login_validator(request.POST)
    if len(login_errors) > 0:
        for key, value in login_errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        email_address = request.POST['email_address']
        request.session['first_name'] = request.POST['email_address']
    return render(request, 'success.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = Register.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        #pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = Register.objects.create(
            first_name=request.POST['first_name'], 
            last_name =request.POST['last_name'],
            email_address=request.POST['email_address'], 
            password=request.POST['password']
        )
        request.session['first_name'] = request.POST['first_name']
    return render(request, 'success.html')