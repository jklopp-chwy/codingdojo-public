from django.shortcuts import render, redirect
from .models import course, courseManager
from django.contrib import messages

def courses(request):
    context = {
        "courses": course.objects.all()
    }
    return render(request, 'index.html', context)

def delete_course(request):
    return render(request, 'index.html')