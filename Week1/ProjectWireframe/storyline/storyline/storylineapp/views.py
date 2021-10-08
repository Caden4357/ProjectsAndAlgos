import os
from django.contrib.messages.api import error
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def index(request):
    # Load login page first thing that comes up 
    return render(request, 'login.html')

# link from not a user sign up here brings you to the register page 
def registerPage(request):
    return render(request, 'register_page.html')

# register new user with validations once successful you will be automatically logged in 
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
        return redirect('/dashboard')

# login in existing user 
def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email_address'], request.POST['password']):
        messages.error(request, "Invalid Email or Password")
        return redirect('/')
    user = User.objects.get(email_address=request.POST['email_address'])
    request.session['user_id'] = user.id
    return redirect('/dashboard')


def logout(request):
    request.session.clear()
    return redirect('/')


# first page user see's on successful log in 
def dashboard(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to log in")
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'stories': Story.objects.all()
    }
    return render(request, 'dashboard.html', context)

# view single users profile page front end validations to give logged in user more freedom over their own account 
def profilePage(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to log in")
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    usersPage =  User.objects.get(id=id)
    context = {
        'usersPage': User.objects.get(id=id),
        'user': user,
        'stories': Story.objects.filter(writer_of_the_story=usersPage)
    }
    return render(request, 'profile.html', context)

# create a new story path in urls.py allows this view to work wether user is on dashboard or profile page 
def new_story(request):
    if 'user_id' not in request.session:
        return redirect('/')
    errors = Story.objects.story_validator(request.POST)
    if errors:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/dashboard')
    else:
        user = User.objects.get(id=request.session['user_id'])
        Story.objects.create(
            title = request.POST['title'],
            genre = request.POST['genre'],
            content = request.POST['content'],
            writer_of_the_story = user
        )
    return redirect('/dashboard')

# you have to click on the title of a story to be able to read it clicking that link will bring you to this page 
def read_one_story(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to log in")
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    story = Story.objects.get(id=id)
    context = {
        'story': story,
        'story_additions': StoryAddition.objects.get(story_trying_to_be_added_to=story),
        'user': user
    }
    return render(request, "single_story.html", context)

# edit story 
def edit(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to log in")
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context ={
        'story': Story.objects.get(id=id),
        'user': user
    }
    return render(request, 'edit_story.html', context)

# update story 
def update(request, id):
    if request.method=="POST":
        errors = Story.objects.story_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/edit/{id}")
        story_to_update = Story.objects.get(id=id)
        story_to_update.title = request.POST['title']
        story_to_update.content = request.POST['content']
        story_to_update.genre = request.POST['genre']
        story_to_update.save()
        return redirect('/dashboard')

# delete story 
def destroy(request, id):
    to_delete = Story.objects.get(id=id)
    to_delete.delete()
    return redirect('/dashboard')


def edit_profile(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to log in")
        return redirect('/')
    user = User.objects.get(id=id)
    context ={
        'user': user
    }
    return render(request, 'edit_profile.html', context)

def update_profile(request, id):
    if request.method=="POST":
        # errors = User.objects.basic_validator(request.POST)
        # if len(errors) > 0:
        #     for key, value in errors.items():
        #         messages.error(request, value)
        #     return redirect(f"/dashboard")
        user = User.objects.get(id=id)
        user_to_update = user
        profile_to_update = Profile.objects.get(user=user)


    # validation to ensure that if the user doesnt change profile picture then it stay what it is originally without throwing multikeydict error 
        if len(request.FILES) != 0:
            if len(profile_to_update.image) > 0:
                profile_to_update.image = profile_to_update.image.path

            profile_to_update.image = request.FILES['image']
        print(profile_to_update.image)
        user_to_update.first_name = request.POST['first_name']
        user_to_update.last_name = request.POST['last_name']
        user_to_update.username = request.POST['username']
        profile_to_update.save()
        user_to_update.save()
        return redirect(f'/profile/{id}')
