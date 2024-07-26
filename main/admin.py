from django.contrib import admin
from .models import Book, Carousel, Category, Author, Publisher, BorrowedBook, BorrowedBookDetail
from slugify import slugify


class BookAdmin(admin.ModelAdmin):
    list_display = ["id","title","isbn","language","created_by","category","pages_count","author","publisher"]
    list_display_links = ["title"]
    exclude = ["created_by", "updated_by"]
    def save_model(self, request, obj, form, change):
        if obj.slug == "":
            obj.slug = slugify(obj.title)
        user = request.user
        obj.created_by = user
        obj.updated_by = user
        super().save_model(request, obj, form, change)
    

class CarouselAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_by","updated_by"]
    list_display_links = ["name"]
    exclude = ["created_by", "updated_by"]
    def save_model(self, request, obj, form, change):
        user = request.user
        obj.created_by = user
        obj.updated_by = user
        super().save_model(request, obj, form, change)
    

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_by", "updated_by"]
    list_display_links = ["name"]

class PublisherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_by", "updated_by"]
    list_display_links = ["name"]

class BorrowedBookAdmin(admin.ModelAdmin):
    exclude = ["created_by","updated_by"]

class BorrowedBookDetailAdmin(admin.ModelAdmin):
    @admin.display
    def returned(obj):
        if obj.returned == None:
            return False
        return obj.returned
    exclude = [ "updated_by"]
    list_display = ["borrowed_book", "book", returned]
    



admin.site.register(Book,BookAdmin)
admin.site.register(Carousel,CarouselAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(BorrowedBook,BorrowedBookAdmin)
admin.site.register(BorrowedBookDetail,BorrowedBookDetailAdmin)

