from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User as Admin

# Create your models here.
class UserManager (models.Manager):
    def register_validator(self, postData):
        errors = {}
        email_match = User.objects.filter(email = postData["email"])
        if len(postData['email'])==0:
            errors["email_blank"] = "Email can not be blank! Please enter email!"
        elif len(email_match) > 0:
            errors["email_invaild"] = "Email exists in database already"
        
        if len(postData['first_name'])==0:
            errors["first_name_blank"] = "First name can not be blank! Please enter a first name!"
        elif len(postData['first_name']) < 2:
            errors["first_name"] = "Fist name should be at least 2 characters"
        if len(postData['last_name'])==0:
            errors["last_name_blank"] = "First name can not be blank! Please enter a first name!"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"    
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors["password_match"] = "Passwords do not match"
        return errors
    
    def login_validator(self, postData):
        login_errors = {}
        # add keys and values to errors dictionary for each invalid field
        user_to_login= User.objects.get(email=postData["email"])
        
        if user_to_login.password != postData['login_password']:
            login_errors["invalid"] = "Invaild login credentials"
        else:
            print("password accepted, logging in ...")
        return login_errors
    
class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 45) 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager() 
    
class Account(models.Model):     
    gpa = models.DecimalField(max_digits = 3, decimal_places = 2)
    test_score = models.IntegerField()
    activities = models.CharField( max_length = 254)
    education_interest = models.CharField( max_length = 254)
    school_int =  models.CharField( max_length = 254)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    
class School(models.Model):
    name = models.CharField(max_length = 45) 
    enrollment = models.CharField(max_length = 254)
    sports = models.CharField(max_length = 254)
    avg_test_score = models.IntegerField()
    gpa = models.DecimalField(max_digits = 3, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
        
class Quote(models.Model):
    text = models.TextField()