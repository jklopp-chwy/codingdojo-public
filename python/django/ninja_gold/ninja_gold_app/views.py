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
        request.session['message'] = ["welcome to ninja gold"]
    return render(request, 'index.html')

def reset(request):
    request.session.clear()
    return redirect('/')

def process_money(request):
    gold_location = request.POST['location'] #sets location 
    gold_range = gold_values[gold_location] #gets int range from location
    gold_amount = random.randint(gold_range[0],gold_range[1]) #selects random int from range
    message_log = [f"you earned {gold_amount}!"]

    #redirect if get
    if request.method == 'GET':
        return redirect('/')
    #handling casino
    if gold_location == 'casino':
        gold_amount = gold_amount * random.randint(-1,1)
        #if you lose money
        if gold_amount < 0:
            message_log = [f"you lost {gold_amount}!"]
            request.session['gold'] += gold_amount
            request.session['message'].append(message_log)
        #if you win money
        else:
            message_log = [f"you earned {gold_amount}!"]
            request.session['gold'] += gold_amount
            request.session['message'].append(message_log)
    #if any other location besides casino
    else:
        request.session['gold'] += gold_amount
        request.session['message'].append(message_log)
    return render(request,'index.html')