from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = (

        'id',
        'title',
        'author',
        'cover_image',
        'published_date',
        'code',
        'created_at'
    )
admin.site.register(Book, BookAdmin)