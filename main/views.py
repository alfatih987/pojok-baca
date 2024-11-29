from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.contrib import messages
from .models import Book, Carousel, Category


def books(request):
    books= Book.objects.all()
    categories = Category.objects.all()
    data ={
        "books":books,
        "categories":categories
    }
    return render(request, 'main/books.html', data)
    
def index(request):
    carousel_images = Carousel.objects.all()
    books = Book.objects.all().order_by('-id')[0:4]
    data = {
        "books":books,
        "carousel":carousel_images,
 
    }
    return render(request, 'main/index.html', data)

def category(request,id):
    books = Book.objects.filter(category=id)
    categories = Category.objects.all()
    data = {
        "books":books,
        "categories":categories
    }

    return render(request, 'main/category.html', data)

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
        return HttpResponseRedirect(reverse("login"))

def book_detail(request, slug_title):
    book = Book.objects.get(slug = slug_title)
    data = {
        "book" : book 
    }
    return render(request, 'main/book_detail.html', data)

def pinjam(request):
    return render(request, 'main/pinjam.html')

