from django.shortcuts import render, redirect
from .models import Register, RegisterManager, Message, Comment
from django.contrib import messages
from django.core.exceptions import ValidationError
import bcrypt

def home(request):
    return render(request, 'index.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def delete_all(request):
    all = Message.objects.all()
    allc = Comment.objects.all()
    all.delete()
    allc.delete()
    return redirect("/profile")

def profile(request):
    context = {
        'messages': Message.objects.all()
    }
    return render(request, 'success.html', context)

def login(request):
    if request.method == "GET":
        return redirect('/')
    login_errors = Register.objects.login_validator(request.POST)
    if len(login_errors) > 0:
        for key, value in login_errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = Register.objects.filter(email_address=request.POST['email_address'])
        user = user[0]
        request.session['first_name'] = user.first_name
        request.session['id'] = user.id
        context = {
        'messages': Message.objects.all()
        }
    return render(request, 'success.html', context)

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
        user = Register.objects.filter(email_address=request.POST['email_address'])
        user = user[0]
        request.session['first_name'] = user.first_name
        request.session['id'] = user.id
    return render(request, 'success.html')

def post(request):
    new_post = Message.objects.create(
        message = request.POST['message'],
        poster = Register.objects.get(id=request.session['id'])
    )
    return redirect('/profile')

def comment(request, id):
    poster = Register.objects.get(id=request.session['id'])
    message = Message.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], poster=poster, wall_message=message)
    return redirect('/profile')
