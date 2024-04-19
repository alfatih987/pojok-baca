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

admin.site.site_header = 'My Project'
admin.site.index_title = 'index 1'
admin.site.site_title = 'HTML tittle'