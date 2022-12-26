from django.shortcuts import render
from viewBooks.models import Book

# Create your views here.
def bookList(request):
    books = Book.objects.all()
    return render(request, 'viewBooks/viewBooks.html', {'books' : books})

def availableBookList(request):
    books = Book.objects.all()
    availableBooks=[]
    for book in books:
        if book.status=='Available':
            availableBooks.append(book)
    return render(request, 'viewBooks/viewAvailableBooks.html', {'books' : availableBooks})
