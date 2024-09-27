from django.db import models
from django.contrib.auth.models import User

 
class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=255,blank=True)
    language = models.CharField(max_length=100)
    pages_count = models.IntegerField()
    abstract = models.TextField()
    isbn = models.CharField(max_length=15)
    cover_image = models.ImageField(upload_to="book_cover/")
    published_date = models.DateField()
    stock = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
        verbose_name= "input by",
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
    def __str__(self):
        return self.title    
    

 
class Carousel(models.Model):
    image = models.ImageField(upload_to="carousel_images/")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)   
    # def __str__(self):
        # return self.image
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        verbose_name= "input by",
        to=User,
        on_delete=models.DO_NOTHING
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)
 
    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name_plural = "Categories"

 
 
class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        verbose_name= "input by",
        to=User,
        on_delete=models.DO_NOTHING
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)  

    def __str__(self):
        return self.name
 
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)
    def __str__(self):
        return self.name
 
class BorrowedBook(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING
    )
    created_by = models.CharField(max_length=100, verbose_name= "librarian",blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)
    def __str__(self):
        return self.member.username
 
class BorrowedBookDetail(models.Model):
    borrowed_book = models.ForeignKey(
        to="BorrowedBook",
        on_delete=models.DO_NOTHING,
    )
    book = models.ForeignKey(
        to="Book",
        on_delete=models.DO_NOTHING,
    )
    
    returned = models.DateTimeField(null=True ,blank = True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)