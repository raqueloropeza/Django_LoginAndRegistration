from django.db import models
from datetime import date, datetime
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name'])<2:
            errors["first_name"] = "First name should be at least 2 characters."
        if len(postData['last_name'])<2:
            errors["last_name"] = "Last name should be at least 2 characters."
        if len(postData['password'])<8:
            errors["email"] = "Password must be 8 characters or more."
        if (postData['confirmpassword'] != postData['password']):
            errors["password"] = "Passwords must match!"

        user = Users.objects.filter(email=postData['email'])
        if user:
            errors["email"] = "Email is already registered. Login with email and password."
         
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Must include a valid email."
        
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    secret_message = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# Create your models here.
