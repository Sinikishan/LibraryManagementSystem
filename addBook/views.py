from django.shortcuts import render
from addBook.forms import AddBookForm
from viewBooks.models import Book

# Create your views here.
def addBookForm(request):
    addForm=AddBookForm()
    if request.method == 'POST':
        addForm= AddBookForm(request.POST)
        if addForm.is_valid():
            title=addForm.cleaned_data['title']
            isbn=addForm.cleaned_data['isbn']
            pages=addForm.cleaned_data['pages']
            year=addForm.cleaned_data['publish_Year']
            author=addForm.cleaned_data['author']
            status="Available"
            newBook=Book(title=title, isbn=isbn, pages=pages, publishYear=year, author=author, status=status)
            newBook.save()
    return render(request, 'addBook/addBookForm.html', {'addForm':addForm})
