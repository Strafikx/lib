from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Books, Author, Publisher
from .forms import BookForm, PublisherForm, AuthorForm

# Create your views here.

def books(request):
    allBooks = Books.objects.all()
    return render(request, 'books/books.html', {'books':allBooks})


def book(request, pk):
    book = Books.objects.get(id=pk)
    return render(request, 'books/single-book.html', {'book': book})


@login_required
def addBook(request):
    form = BookForm()
    if request.method == 'POST':
        print(request.POST)
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books')

    
    context = {'form':form}
    return render(request,'books/book-form.html', context)


@login_required
def editBook(request, pk):
    book = Books.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        print(request.POST)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')

    
    context = {'form':form}
    return render(request,'books/book-form.html', context)


def authors(request):
    allAuthors = Author.objects.all()
    return render(request, 'books/authors.html', {'authors':allAuthors})


@login_required
def addAuthor(request):
    form = AuthorForm()
    if request.method == 'POST':
        print(request.POST)
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')

    
    context = {'form':form}
    return render(request,'books/author-form.html', context)


def publishers(request):
    allPublishers = Publisher.objects.all()
    return render(request, 'books/publishers.html', {'publishers':allPublishers})


@login_required
def addPublisher(request):
    form = PublisherForm()
    if request.method == 'POST':
        print(request.POST)
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publishers')

    
    context = {'form':form}
    return render(request,'books/publisher-form.html', context)


