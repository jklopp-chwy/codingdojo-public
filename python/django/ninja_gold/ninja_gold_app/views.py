#python manage.py migrate
#python3 -m venv djangoPy3Env 
# pip install Django==2.2 
#django-admin startproject your_project_name_here
#python manage.py startapp your_app_name_here
#add new project to settings.py

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
import random

gold_values = {
    "farm": (10,20),
    "cave": (5,10),
    "house": (2,5),
    "casino": (0,50)
}

# Create your views here.
def index(request):
    if not "gold" in request.session or "message" in request.session:
        request.session['gold'] = 0
        request.session['message'] = "welcome to ninja gold"
    return render(request, 'index.html')

def reset(request):
    request.session.clear()
    return redirect('/')

def process_money(request):
    message_log = request.POST['message']
    gold_location = request.POST['location']
    gold_range = gold_values[gold_location]
    gold_amount = random.randint(gold_range[0],gold_range[1])


    if request.method == 'GET':
        return redirect('/')
    else:
        request.session['gold'] += gold_amount
        request.session['message'] = message_log.append()
    return render(request,'index.html')