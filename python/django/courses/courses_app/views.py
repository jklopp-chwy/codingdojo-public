from django.shortcuts import render, redirect
from .models import Course, CourseManager
from django.contrib import messages

def courses(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'index.html', context)

def create_courses(request):
    errors = Course.objects.basic_validator(request.POST)
    if request.method == 'GET':
        return redirect('/')
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        new_Course = Course.objects.create(
        name = request.POST['name'], 
        description =request.POST['description']
        )
    return redirect("/")

def delete_courses(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, 'delete.html', context)

def delete_course_from_db (request, id):
    if request.method == "POST":
        course = Course.objects.get(id=id)
        course.delete()
    return redirect("/")