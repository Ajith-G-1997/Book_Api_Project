
from django.contrib import admin
from .models import Author, Book,Store

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_books')

    filter_horizontal = ('books',)

    def display_books(self, obj):
        return ", ".join([book.title for book in obj.books.all()])
    display_books.short_description = 'Books'

admin.site.register(Store, StoreAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
