from django.contrib import admin
from .models import Book,Carousel


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

class CarouselAdmin(admin.ModelAdmin):
    list_display = (
        'image',
    )
admin.site.register(Book, BookAdmin)
admin.site.register(Carousel, CarouselAdmin)

admin.site.site_header = 'My Project'
admin.site.index_title = 'index 1'
admin.site.site_title = 'HTML tittle'

