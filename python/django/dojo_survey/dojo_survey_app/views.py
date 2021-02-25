from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    if request.method == 'GET':
        return redirect('/')
    context = {
        "fname": request.POST["fname"],
        "lname": request.POST["lname"],
        "dojos": request.POST["dojos"],
        "gender": request.POST["gender"],
    }
    return render(request, "result.html", context)