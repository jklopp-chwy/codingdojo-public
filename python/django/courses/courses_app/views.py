from django.shortcuts import render, redirect
from .models import course, courseManager
from django.contrib import messages

def courses(request):
    context = {
        "courses": course.objects.all()
    }
    return render(request, 'index.html', context)

def create_courses(request):
    errors = course.objects.basic_validator(request.POST)
    if request.method == 'GET':
        return redirect('/')
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        new_course = course.objects.create(
        name = request.POST['name'], 
        description =request.POST['description']
        )
    return redirect("/")

def delete_courses(request, id):
    context = {
        "courses": course.objects.get(id=id)
    }
    return render(request, 'delete.html', context)