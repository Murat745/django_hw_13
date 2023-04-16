from django.db.models import Count, Prefetch
from django.shortcuts import get_object_or_404, render

from .models import Author, Book, Publisher, Store


def index(request):
    return render(request, 'bookstore/index.html')


def book_list(request):
    books = Book.objects.select_related('publisher').prefetch_related('authors').all()
    return render(request, 'bookstore/book_list.html', {'books': books})


def book(request, pk):
    book_obj = get_object_or_404(Book.objects.select_related('publisher'), pk=pk)
    stores = Store.objects.filter(books=book_obj)
    return render(request, 'bookstore/book_detail.html', {'book': book_obj, 'stores': stores})


def author_list(request):
    authors = Author.objects.prefetch_related(Prefetch('book_set', queryset=Book.objects.only('name')))
    return render(request, 'bookstore/author_list.html', {'authors': authors})


def author(request, pk):
    author_obj = get_object_or_404(Author, pk=pk)
    books = Book.objects.filter(authors=author_obj)
    return render(request, 'bookstore/author_detail.html', {'author': author_obj, 'books': books})


def publisher_list(request):
    publishers = Publisher.objects.prefetch_related('book_set')
    return render(request, 'bookstore/publisher_list.html', {'publishers': publishers})


def publisher(request, pk):
    publisher_obj = get_object_or_404(Publisher, pk=pk)
    books = Book.objects.filter(publisher=publisher_obj)
    return render(request, 'bookstore/publisher_detail.html', {'publisher': publisher_obj, 'books': books})


def store_list(request):
    stores = Store.objects.annotate(num_books=Count('books')).all()
    return render(request, 'bookstore/store_list.html', {'stores': stores})


def store(request, pk):
    store_obj = get_object_or_404(Store, pk=pk)
    return render(request, 'bookstore/store_detail.html', {'store': store_obj})
