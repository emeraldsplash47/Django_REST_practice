from django.shortcuts import render
from books.models import Book
from django.views.generic import ListView


class BookListView(ListView):
    model = Book
    templete_name = 'book_list.html'


