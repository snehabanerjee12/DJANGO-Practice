from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
]


"""
path('books/', ...) — matches the URL /books/ exactly
path('books/<int:pk>/', ...) — <int:pk> is a path converter: it captures a number from the URL and passes it to the view as an argument called pk. So visiting /books/3/ calls book_detail(request, pk=3).
name='book_list' — a named URL. Instead of hardcoding /books/ everywhere (templates, redirects), you reference it by name — if the URL path ever changes, you only update it in one place. Interviewers often ask why you'd use named URLs instead of hardcoded strings — this is the answer.
"""