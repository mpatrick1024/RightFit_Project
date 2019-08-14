from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import random
from .models import *

# Create your views here.
def index(request):
    all_users = User.objects.all().values()
    all_quotes = Quote.objects.all()
    index = random.randint(0, len(all_quotes)-1)
    quote = all_quotes[index]
    context = {
        "quote" : quote, 
        "users": all_users
    }
    return render (request, 'rightfit_app/index.html', context)

def register (request):
    errors = User.objects.register_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value, extra_tags='errors')
        # redirect the user back to the form to fix the errors
        return redirect('/register')
        
    else:
        User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
        last_user = User.objects.last()
        request.session["user_id"]= last_user.id
        request.session["user_name"]= last_user.first_name
    return redirect('/loading')


def register_form(request):
    all_users = User.objects.all().values()
    all_quotes = Quote.objects.all()
    index = random.randint(0, len(all_quotes)-1)
    quote = all_quotes[index]
    context = {
        "quote" : quote, 
        "users": all_users
    }
    return render (request, 'rightfit_app/register.html', context)

def login_form(request):
    all_users = User.objects.all().values()
    all_quotes = Quote.objects.all()
    index = random.randint(0, len(all_quotes)-1)
    quote = all_quotes[index]
    context = {
        "quote" : quote, 
        "users": all_users
    }
    return render (request, 'rightfit_app/login.html', context)

def login (request):
    login_errors = User.objects.login_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(login_errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in login_errors.items():
            messages.error(request, value, extra_tags='login_errors')
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        user = User.objects.get(login_email=request.POST["login_email"])
        request.session["user_id"]= user.id
        return redirect('/loading')
    
def accountpage (request):
        user = User.objects.get(id=request.session["user_id"])
        all_quotes = Quote.objects.all()
        all_schools = School.objects.all()

            
        for school in all_schools:
            print (school.id, school.name)
        
        index = random.randint(0, len(all_quotes)-1)
        quote = all_quotes[index]
        context = {
        "user" : user,
        "quote" : quote,

    }
        return render(request, 'rightfit_app/accountpage.html', context)

def account_edit_form(request):
        user_update = User.objects.get(id=request.session["user_id"])
        user_update.first_name= request.POST["first_name"]
        user_update.last_name= request.POST["last_name"]
        user_update.email= request.POST["email"]
        user_update.activities= request.POST["activities"]
        user_update.education_interest= request.POST["education_interest"]
        user_update.school_int= request.POST["school_int"]
        user_update.save()
        return redirect('/')
    
def loading(request):
    all_quotes = Quote.objects.all()
    index = random.randint(0, len(all_quotes)-1)
    quote = all_quotes[index]
    context ={
        "quote" : quote
    }
    return render(request, 'rightfit_app/loading.html', context )

def schoolchoices(request):
    interest1 = School.objects.get(id=request.POST["school_int1"])
    interest2 = School.objects.get(id=request.POST["school_int2"])
    interest3 = School.objects.get(id=request.POST["school_int3"])
    all_quotes = Quote.objects.all()
    index = random.randint(0, len(all_quotes)-1)
    quote = all_quotes[index]
    context ={
        "quote" : quote,
        "interest1" : interest1,
        "interest2" : interest2,
        "interest3" : interest3
    }
    return render(request, 'rightfit_app/schoolchoices.html', context)

def profile (request):
    user = User.objects.get (id=request.session["user_id"])
    context = {
        "user": user
    }
    return render (request, "rightfit_app/profile.html", context)

def schoolmatches(request):
    all_quotes = Quote.objects.all()
    index = random.randint(0, len(all_quotes)-1)
    quote = all_quotes[index]
    context ={
        "quote" : quote
    }
    return render(request, 'rightfit_app/schoolmatches.html', context)