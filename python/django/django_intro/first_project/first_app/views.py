from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs with a method named index")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog with a method named new")

def create(request):
    return redirect('/')

def number(request, number):
    return HttpResponse(f"placeholder to display blog number: {number} with a method named show")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number} with a method named edit")

def destroy(request, number):
    return redirect('/')