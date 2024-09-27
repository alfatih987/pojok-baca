from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('register/', views.register, name="register"  ),
    path('book/detail/<int:id>', views.book_detail, name="book_detail"),
    path('books/', views.books, name="books" )
]
