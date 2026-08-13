from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Book, Author, Member, BorrowRecord

# Create your views here.
def book_list(request):
    books = Book.objects.select_related('author').all()
    output = "<h1>Book List</h1><ul>"
    for book in books:
        output += f"<li>{book.title} - by {book.author.name}</li>"
    output += "</ul>"
    return HttpResponse(output)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    output = f"<h1>{book.title}</h1><p>Author: {book.author.name}</p><p>ISBN: {book.isbn}</p><p>Total Copies: {book.total_copies}</p>"
    return HttpResponse(output)


"""
select_related('author') — remember Module 2? We use it here specifically because we access book.author.name inside a loop — without it, you'd get an N+1 query. This is the real place that matters, not just theory.
get_object_or_404(Book, pk=pk) — tries to fetch a Book by primary key; if it doesn't exist, automatically returns a proper 404 page instead of crashing with an unhandled exception. This is the standard, correct way to fetch a single object in a view — always prefer this over Book.objects.get(pk=pk) directly, because .get() alone raises an ugly DoesNotExist error if the row isn't found.
"""