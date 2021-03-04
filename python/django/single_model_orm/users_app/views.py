from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
import random
from .models import Users

# Create your views here.
def index(request):
    context = {
    	"all_the_users": Users.objects.all()
    }
    return render(request, 'index.html', context)

def reset(request):
    request.session.clear()
    return redirect('/')

def add_user(request):
    if request.method == 'GET':
        return redirect('/')
    else:
        new_user = Users.objects.create(
            first_name=request.POST['first_name'], 
            last_name =request.POST['last_name'],
            email_address=request.POST['email_address'], 
            age=request.POST['age'])
    return redirect('/')