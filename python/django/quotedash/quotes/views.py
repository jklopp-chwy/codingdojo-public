from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Quote
# Create your views here.
def index(request):
    return render(request, 'index.html')

def delete_all(request):
    all = Quote.objects.all()
    all.delete()
    return redirect("/")

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('/quotes')

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "You have successfully logged in!")
    return redirect('/quotes')

def logout(request):
    request.session.clear()
    return redirect('/')

def quotes(request):
    if 'user_id' not in request.session:
        return redirect('/')

    user = User.objects.get(id=request.session['user_id'])
    quotes = Quote.objects.all()

    quoteLikes = Quote.objects.get

    context = {
        'user': user,
        'quotes': quotes

    }
    return render(request, 'quotes.html', context)

def add_quote(request):
    errors = Quote.objects.addQuote(request.POST)
    if request.method == "GET":
        return redirect('/quotes')
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/quotes')
    new_quote = Quote.objects.create(
        author = request.POST['author'],
        quote = request.POST['quote'],
        uploaded_by = User.objects.get(id=request.session['user_id'])
    )
    return redirect('/quotes')

def edit_account(request, id):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'quotes': Quote.objects.filter(id=request.session['user_id'])
    }
    return render(request, 'edit.html', context)

def update_account(request):
    errors = User.objects.editUser(request.POST)
    if request.method == "GET":
        return redirect('/quotes')
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/quotes')
    edit_user = User.objects.get(id=request.session['user_id'])
    edit_user.first_name= request.POST['first_name']
    edit_user.last_name= request.POST['last_name']
    edit_user.email=request.POST['email']
    edit_user.save()
    return redirect('/quotes')

def delete_quote(request, id):
    edit_quote = Quote.objects.get(id=id)
    edit_quote.delete()
    return redirect("/quotes")

def user(request, id):
    context = {
        'user': User.objects.get(id=id),
    }
    return render(request, 'user.html', context)

def like_quote(request, id):
    user = User.objects.get(id=request.session['user_id'])
    quote = Quote.objects.get(id=id)
    user.liked_quotes.add(quote)
    return redirect("/quotes")