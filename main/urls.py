from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('register/', views.register, name="register"  ),
    path('book/detail/<slug:slug_title>', views.book_detail, name="book_detail"),
    path('books/', views.books, name="books" ),
    path('category/<int:id>', views.category, name="category"),
    path('pinjam/', views.pinjam, name="pinjam" ),
    path('account/',views.account, name="account"),
    path('account/my-borrowings', views.my_borrowings, name="borrowings"),
    path('admin-dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('admin-borrowings/', views.admin_borrowings, name="admin_borrowings"),
    path('login/', views.auth_login, name="login")

    

]
