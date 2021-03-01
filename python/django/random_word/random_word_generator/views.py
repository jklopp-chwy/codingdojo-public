#python manage.py migrate
#python3 -m venv djangoPy3Env 
# pip install Django==2.2 
#django-admin startproject your_project_name_here
#python manage.py startapp your_app_name_here
#add new project to settings.py

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    request.session['counter'] = 0
    #counter = request.session.get('counter', 0)
    return render(request, "index.html")

def random_word(request):
    if request.method == 'GET':
        return redirect('/')
    else:
        request.session['random_word'] = get_random_string(length=14)
        request.session['counter'] += 1
    return render(request,'random_word.html')

def reset(request):
    request.session.flush()
    return redirect('/')