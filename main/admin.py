from django.contrib import admin
from .models import Book, Carousel, Category, Author, Publisher, BorrowedBook, BorrowedBookDetail
from slugify import slugify
import datetime


class BookAdmin(admin.ModelAdmin):
    list_display = ["id","title","isbn","language","created_by","category","pages_count","author","publisher","stock"]
    list_display_links = ["title"]
    exclude = ["created_by", "updated_by"]
    def save_model(self, request, obj, form, change):
        if obj.slug == "":
            obj.slug = slugify(obj.title)
        user = request.user
        obj.created_by = user
        obj.updated_by = user.username
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
    exclude = ["created_by","updated_by"]
    def save_model(self, request, obj, form, change):
        user = request.user
        obj.created_by = user
        obj.updated_by = user
        super().save_model(request, obj, form, change)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_by", "updated_by"]
    list_display_links = ["name"]
    exclude = ["created_by","updated_by"]
    def save_model(self, request, obj, form, change):
        user = request.user
        obj.created_by = user
        obj.updated_by = user
        super().save_model(request, obj, form, change)

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

    def delete_model(self, request, obj):
        if obj.returned is not None:
            obj.delete()

    

    
    def get_form(self, request, obj=None, **kwargs):
        form =super().get_form(request, obj,  **kwargs)
        form.base_fields["book"].queryset  = Book.objects.filter(stock__gt=0)
        return form

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        book_id = obj.book.id
        book_object = Book.objects.get(id=book_id)
        if obj.returned == None:
            book_object.stock -= 1
        else:
            book_object.stock += 1
        book_object.save()
        
    

        
        

    @admin.action(description="Mark selected as returned")
    def make_return(modeladmin, request, queryset):
        for obj in queryset:
            book_id = obj.book.id
            book_object = Book.objects.get(id=book_id)
            if book_object is None:
                book_object.stock += 1
            book_object.save()
        queryset.update(returned=datetime.datetime.now())
        


    @admin.action(description="Mark selected as unreturned")
    def make_unreturn(modeladmin, request, queryset):
        for obj in queryset:
            book_id = obj.book.id
            book_object = Book.objects.get(id=book_id)
            if book_object is not None:
                book_object.stock += 1
            book_object.save()
        queryset.update(returned=None)


    actions = [make_unreturn, make_return]









admin.site.register(Book,BookAdmin)
admin.site.register(Carousel,CarouselAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(BorrowedBookDetail,BorrowedBookDetailAdmin)
admin.site.register(BorrowedBook,BorrowedBookAdmin)

