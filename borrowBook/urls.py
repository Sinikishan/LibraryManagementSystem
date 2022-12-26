from django.urls import path
from . import views

app_name='borrowBook'
urlpatterns = [
    path('/<int:passedISBN>', views.borrowBook, name="borrowPage"),
    path('/borrowedBooks', views.showBorrowedBooks, name="borrowedBooks"),
]
