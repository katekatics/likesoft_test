from django.contrib import admin
from book_manager.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "author", "pub_year", "isbn"]
    ordering = ["pub_year"]


admin.site.register(Book, BookAdmin)
