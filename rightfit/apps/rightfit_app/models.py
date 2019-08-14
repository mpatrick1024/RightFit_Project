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
        user_to_login= User.objects.filter(email=postData["login_email"])
        if len(postData['login_email']) == 0:
            print ('Did not find email in database')
            login_errors['invalid'] = 'Invalid login credentials'
        else:
            user = User.objects.get (email = postData['login_email'])
            if postData['login_password'] == user.password:
                print('Valid password, Login Success')
            else:
                print("Invalid password, Login Unsuccessful")
                login_errors['invalid'] = "Invalid login credentials."
        return login_errors
    
    def student_validator(self, postData):
        student_errors ={}
        # add keys and values to errors dictionary for each invalid field
        
        if len(postData['gpa']) ==0:
            student_errors['gpa_blank'] = 'Gpa can not be blank!!'
        elif len(postData['gpa']) > 3:
            student_errors['gpa_length'] = 'Gpa can not be more than 3 digits!!'
        if len(postData['test_score']) ==0:
            student_errors['test_score_blank'] = 'Test Score can not be blank!!' 
        if (postData['test_score']) > 900 :
            student_errors['test_score_num'] = 'Test Score is invaild !!' 
        
class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 45) 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager() 
    
class Activity(models.Model):
    name = models.CharField(max_length = 254) 
    
class Major(models.Model):
    name = models.CharField(max_length = 254)
    
class Student(models.Model):     
    gpa = models.DecimalField(max_digits = 3, decimal_places = 2)
    test_score = models.IntegerField()
    parent =  models.ForeignKey(User, related_name ="students")
    activities =  models.ManyToManyField(Activity, related_name ="students")
    majors = models.ForeignKey( Major, related_name ="students")
    school_int =  models.CharField( max_length = 254)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    
class School(models.Model):
    name = models.CharField(max_length = 45) 
    enrollment = models.CharField(max_length = 254)
    activities = models.ManyToManyField(Activity, related_name ="schools")
    avg_test_score = models.IntegerField()
    majors = models.ManyToManyField( Major, related_name ="schools")
    gpa = models.DecimalField(max_digits = 3, decimal_places = 2)
    students = models.ManyToManyField(Student, related_name ="schools")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
        
class Quote(models.Model):
    text = models.TextField()
