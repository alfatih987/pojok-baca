from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test 
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.contrib import messages
from .models import Book, Carousel, Category, BorrowedBook, BorrowedBookDetail
from django.contrib.auth import update_session_auth_hash
from django.utils.dateparse import parse_date
from django.shortcuts import render, redirect
from datetime import datetime, time
from django.contrib.auth import authenticate, login, logout

def books(request):
    books= Book.objects.all()
    categories = Category.objects.all()
    data ={
        "books":books,
        "categories":categories
    }
    return render(request, 'main/books.html', data)
    
def index(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')

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

def auth_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'registration/login.html')

def book_detail(request, slug_title):
    book = Book.objects.get(slug = slug_title)
    data = {
        "book" : book 
    }
    
    return render(request, 'main/book_detail.html', data)

def pinjam(request):
    book_id = request.POST.get('book_id')
    book = Book.objects.get(id=book_id)
    #cek buku stok
    if book.stock < 1:
        messages.error(request,"buku ini sudah habis")
        return HttpResponseRedirect(f"/book/detail/{book.slug}")
    #update data stock
    else:
        book.stock -= 1
        book.save()

    borrowed_book = BorrowedBook.objects.create(
        member = request.user,
        created_by = f"User: {request.user.first_name}{request.user.last_name}",
    )
 
    # tambah data borrowed book detail
    borrowed_book_detail = BorrowedBookDetail(
        borrowed_book = borrowed_book,
        book = book
    ).save()    

    messages.success(request,"kamu berhasil meminjam buku ini silahkan menghubungi admin untuk meminjam nya")
    return HttpResponseRedirect(f"/book/detail/{book.slug}")

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
    borrowedBooks = BorrowedBook.objects.filter(member=request.user).prefetch_related('borrowedbookdetail_set').order_by('-date')

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date:
        borrowedBooks = borrowedBooks.filter(date__gte=datetime.combine(parse_date(start_date), time.min))
    if end_date:
        borrowedBooks = borrowedBooks.filter(date__lte=datetime.combine(parse_date(end_date), time.max))

    context = {
        "borrowedBooks": borrowedBooks,
        "start_date": start_date,
        "end_date": end_date,
    }
    return render(request, 'main/borrowings.html', context)

def is_admin(user):
     return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    total_users = User.objects.filter(is_staff=False).count()
    total_books = Book.objects.count()
    total_borrowed_books = BorrowedBookDetail.objects.filter(returned__isnull=True).count()
    total_borrowings = BorrowedBook.objects.count()
    data = {
        "total_users" : total_users,
        "total_books" : total_books,
        "total_borrowed_books" : total_borrowed_books,
        "total_borrowings" : total_borrowings
    }

    return render(request,'admin/dashboard.html', data)

@login_required
@user_passes_test(is_admin)
def admin_borrowings(request):
    

    return render(request,'admin/borrowings.html',)
    
