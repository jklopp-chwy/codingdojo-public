#python manage.py migrate
#python3 -m venv djangoPy3Env 
# pip install Django==2.2 
#django-admin startproject your_project_name_here
#python manage.py startapp your_app_name_here
#add new project to settings.py

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    if request.method == 'GET':
        return redirect('/')
    else:
        request.session['fname'] = request.POST['fname']
        request.session['lname'] = request.POST['lname']
        request.session['dojos'] = request.POST['dojos']
        request.session['gender'] = request.POST['gender']
        request.session['food'] = request.POST.getlist("food[]")
        request.session['counter'] = 100
    return redirect('/')