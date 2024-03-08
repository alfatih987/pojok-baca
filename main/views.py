from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.contrib import messages

@login_required
def index(request):
    return HttpResponse("homepage")

def register(request):
    if request.method == 'GET':
        return render(request,'registration/register.html')
    else :
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        username = request.POST['username']

        if password != password2:
            messages.error(request,'password is not the same')
            return render(request, 'registration/register.html')

        user = User(
            first_name = firstname,
            last_name = lastname,
            email = email,
            username = username,
            password = make_password(password)

        )
        user.save()
        messages.success(request,'your account have been created')
        return render(request, 'registration/login.html')



