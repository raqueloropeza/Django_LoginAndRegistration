from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users
import bcrypt
import re

#main route renders login and registration template
def index(request):
    return render(request, "login.html")

#register route creates new user record in database
def register(request):
    #Retrieve any errors from validations in models
    errors = Users.objects.basic_validator(request.POST)
    #If there are errors from model, redirect to main route and display error messages. 
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    #If there are no errors found, retrieve password from POST data and encrypt.
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        #Retrieve encrypted password and input fields from POST data to create new user record in database.
        this_user = Users.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email= request.POST['email'], secret_message = request.POST['secret_message'], password= pw_hash)
        #Put new user id in session
        request.session['user_id'] = this_user.id
        print(this_user.id)
        #redirect to success route
        return redirect('/success')

#Success route renders template that displays user info
def success(request):
    #Check to make sure user id is in session.  If no user id is in session, redirect to main route. 
    if "user_id" not in request.session:
        return redirect('/')
    #If user id is in session, retrieve user record to display in template.
    else: 
        context = {
            "user": Users.objects.get(id= request.session['user_id'])
        }
        return render(request, "success.html",context)
#Logout route clears user id in session and redirects to main route
def logout(request):
    del request.session['user_id']
    return redirect('/')

#Login route takes email from POST data and filters through user object to try to find matching email
def login(request):
    user =  Users.objects.filter(email=request.POST['email'])
    #If matching email in user object is found, check to see if password from POST data matches password from user object
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            #if passwords match, put user id in session and redirect to success route
            request.session['user_id'] = logged_user.id
            return redirect('/success')
        #if passwords don't match, redirect to main route and display message error.
        else:
            messages.error(request, "invalid login")
            return redirect('/')
        