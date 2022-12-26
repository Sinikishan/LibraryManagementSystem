from django.urls import path
from . import views

app_name='viewBooks'
urlpatterns = [
    path('', views.bookList, name="homePage"),
    path('availableBooks', views.availableBookList, name="availableBooks")
]
