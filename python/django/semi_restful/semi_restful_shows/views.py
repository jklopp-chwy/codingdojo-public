from django.shortcuts import render, redirect
from .models import Show

def shows(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, 'index.html', context)

def get_shows(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, 'show.html', context)

def delete_shows(request, id):
    if request.method == "POST":
        show = Show.objects.get(id=id)
        show.delete()
    return redirect("/")
