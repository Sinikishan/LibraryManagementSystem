from django.shortcuts import render, redirect
from viewBooks.models import Book
from borrowBook.models import Borrower
from borrowBook.forms import BorrowForm
from datetime import date, timedelta, datetime

# Create your views here.
def borrowBook(request, passedISBN):
    book = Book.objects.get(isbn=passedISBN)
    borrowForm=BorrowForm()
    if request.method == 'POST':
        borrowForm=BorrowForm(request.POST)
        if borrowForm.is_valid():
            studentID=borrowForm.cleaned_data['student_id']
            isbn=passedISBN
            title=book.title
            name=borrowForm.cleaned_data['name']
            email=borrowForm.cleaned_data['email']
            phone=borrowForm.cleaned_data['phone']
            today=date.today()
            borrowDate=today.strftime("%d/%m/%Y")
            after30Days = today+ timedelta(days=30)
            returnDate=after30Days.strftime("%d/%m/%Y")
            borrower=Borrower(student_id=studentID, email=email, phone=phone, borrow_date=borrowDate, return_date=returnDate, isbn=isbn, title=title, name=name)
            borrower.save()
            book.status="Borrowed"
            book.save()
            return redirect('/borrow/borrowedBooks')
    return render(request, 'borrowBook/borrowBook.html', {'book' : book, 'borrowForm':borrowForm})


def showBorrowedBooks (request):
    borrowList=Borrower.objects.all()
    filteredBorrowList=[]
    for item in borrowList:
        returnDateString=item.return_date
        returnDateDate=datetime.strptime(returnDateString, '%d/%m/%Y').date()
        if returnDateDate>date.today():
            filteredBorrowList.append(item)
        else:
            book=Book.objects.get(isbn=item.isbn)
            if book.status!="Available":
                book.status="Available"
                book.save()
    return render(request, 'borrowBook/showBorrowedBooks.html', {'borrowList':filteredBorrowList})
