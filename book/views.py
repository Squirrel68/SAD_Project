from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.

# Hiển thị danh sách sách
def book_list(request):
    books = Book.objects.all()
    return render(request, "book/book_list.html", {"books": books})

# Hiển thị chi tiết sách
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "book/book_detail.html", {"book": book})

