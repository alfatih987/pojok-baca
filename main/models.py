from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length= 50)
    cover_image = models.ImageField(upload_to="book_cover")
    published_date = models.DateTimeField()
    code = models.CharField(max_length=10)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        null = True,
        blank = True

    )
    created_at = models.DateTimeField()

class Carousel(models.Model):
    image = models.ImageField(upload_to="")
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

