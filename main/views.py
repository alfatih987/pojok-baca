from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.contrib import messages
from .models import Book, Carousel, Category, BorrowedBook, BorrowedBookDetail
from django.contrib.auth import update_session_auth_hash


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
    book = Book.objects.get(id=request.POST['book.id'])
    #cek buku stok
    if book.stock < 1:
        messages.error(request,"buku ini sudah habis")
        return HttpResponseRedirect(f"/book/detail/{book.slug}")
    #update data stock
    else:
        book.stock = book.stock -1
        book.save()

    borrowed_book = BorrowedBook.objects.create(
        member = request.user,
        created_by = f"User: {request.user.first_name}{request.user.last_name}"
    )
 
    # tambah data borrowed book detail
    borrowed_book_detail = BorrowedBookDetail(
        borrowed_book = borrowed_book,
        book = book
    ).save()    



def account(request):
    
    if request.method == "POST" :
        user = User.objects.get(id=request.POST['id'])
        
        id = request.POST['id']
        username = request.POST['username']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        
        user.id = id
        user.username = username
        user.first_name = firstName
        user.last_name = lastName
        user.email = email
        if len(password1) > 3 and password1 == password2:
            user.password = make_password(password1)
            update_session_auth_hash(request, user)
        user.save()
        update_session_auth_hash(request, user)
        print(f"ur :{user}")
        # return HttpResponseRedirect(reverse("login"))
        
             
    
    account = User.objects.get(id = request.user.id)
        
    print(request.user)
    print(account.id)
    data = {
        "user" : account
    }
    return render(request, 'main/account.html', data)

def my_borrowings(request):
    borrowedBooks = BorrowedBook.objects.filter(member = request.user)
    # borrowedBookDetails = BorrowedBookDetail.objects.filter(borrowed_book = borrowedBooks.id)

    data = {
        "borrowedBooks" : borrowedBooks,
        # "borrowings" : borrowedBookDetails
    }

    return render(request, 'main/borrowings.html', data)