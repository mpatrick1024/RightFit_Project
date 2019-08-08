from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from .models import *
# Create your views here.
def index(request):
    all_users = User.objects.all().values()
    context = {
        "users": all_users
    }
    return render (request, 'rightfit_app/index.html')

def register (request):
    errors = User.objects.register_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value, extra_tags='errors')
        # redirect the user back to the form to fix the errors
        return redirect('/')
        
    else:
        User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
        last_user = User.objects.last()
        request.session["user_id"]= last_user.id
        request.session["user_name"]= last_user.first_name
    return redirect('/success')

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
        user = User.objects.get(email=request.POST["email"])
        request.session["user_id"]= user.id
        return redirect('/success')
    
    def edit_account(request):
        user = User.objects.get(id=request.session["user_id"])
    context = {
        "user" : user
    }
    return render(request, 'rightfit_app/edit_account.html', context)

def account_edit_form(request):
    user_update = User.objects.get(id=request.session["user_id"])
    user_update.first_name= request.POST["first_name"]
    user_update.last_name= request.POST["last_name"]
    user_update.email= request.POST["email"]
    user_update.activities= request.POST["activities"]
    user_update.education_interest= request.POST["education_interest"]
    user_update.school_int= request.POST["school_int"]
    user_update.save()
    return redirect('/edit_account')

def profile (request):
    user = User.objects.get (id=request.session["user_id"])
    context = {
        "user": user
    }
    return render (request, "rightfit_app/profile.html", context)