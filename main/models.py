from django.db import models
from django.contrib.auth.models import User
 
class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.TextField()
    language = models.CharField(max_length=100)
    pages_count = models.IntegerField()
    abstract = models.TextField()
    isbn = models.CharField(max_length=13)
    cover_image = models.ImageField(upload_to="book_cover/")
    published_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)
    category = models.ForeignKey(
        to="Category",
        on_delete=models.DO_NOTHING,
    )
    author = models.ForeignKey(
        to="Author", 
        on_delete=models.DO_NOTHING,     
    )
    publisher = models.ForeignKey(
        to="Publisher",
        on_delete=models.DO_NOTHING
    )    
 
class Carousel(models.Model):
    image = models.ImageField(upload_to="carousel_images/")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)   
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)
 
    def __str__(self):
        return self.name
 
    class meta:
        verbose_name__plural = "Categories"
 
 
class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)  
 
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)
 
class Borrowed_book(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING
    )
    librarian = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)
 
class Borrowed_book_detail(models.Model):
    borrowed_book = models.ForeignKey(
        to="Borrowed_book",
        on_delete=models.DO_NOTHING,
    )
    book = models.ForeignKey(
        to="Book",
        on_delete=models.DO_NOTHING,
    )
    returned = models.DateTimeField(default=None)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)