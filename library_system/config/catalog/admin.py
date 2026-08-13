from django.contrib import admin
from .models import Author, Book, Member, BorrowRecord


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'total_copies') # display these fields in the list view
    search_fields = ('title', 'isbn') # allow searching by title and isbn
    list_filter = ('author',) # allow filtering by author

# Register your models here.
admin.site.register(Author)
admin.site.register(Member)
admin.site.register(BorrowRecord)