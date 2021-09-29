from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'login.html')

def registerPage(request):
    return render(request, 'register_page.html')

def register(request):
    if request.method == "GET":
        return redirect('/registerPage')
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/registerPage')
    else:
        user = User.objects.register(request.POST)
        request.session['user_id'] = user.id
        return redirect('/success')


def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email_address'], request.POST['password']):
        messages.error(request, "Invalid Email or Password")
        return redirect('/')
    user = User.objects.get(email_address=request.POST['email_address'])
    request.session['user_id'] = user.id
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')


def registered(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to log in")
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'user_page.html', context)
