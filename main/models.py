from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length= 50)
    cover_image = models.ImageField(upload_to="book_cover")
    published_date = models.DateTimeField()
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    

