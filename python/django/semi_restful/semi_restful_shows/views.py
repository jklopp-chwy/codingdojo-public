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

def new_shows(request):
    return render(request, 'new.html')

def create_shows(request):
    if request.method == 'GET':
        return redirect('/')
    else:
        new_show = Show.objects.create(
        title=request.POST['title'], 
        description =request.POST['description'],
        network=request.POST['network'], 
        release_date=request.POST['release_date']
        )
    return redirect("/")

def edit_shows(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def edit(request, id):
    if request.method == "POST":
        show = Show.objects.get(id=id)
        show.title = request.POST['title'],
        show.description = request.POST['description'],
        show.network = request.POST['network'],
        show.release_date = request.POST['release_date']
        show.save()
    return redirect(f"/shows/{id}")