from django.urls import path
from . import views

app_name='addBook'
urlpatterns = [
    path('', views.addBookForm, name='addBookPage'),
]
