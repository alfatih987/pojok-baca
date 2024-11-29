from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('register/', views.register, name="register"  ),
    path('book/detail/<slug:slug_title>', views.book_detail, name="book_detail"),
    path('books/', views.books, name="books" ),
    path('category/<int:id>', views.category, name="category"),
    path('pinjam/', views.pinjam, name="pinjam" )

]
