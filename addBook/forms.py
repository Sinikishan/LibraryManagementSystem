from django import forms

class AddBookForm(forms.Form):
    title=forms.CharField()
    isbn=forms.IntegerField()
    author=forms.CharField()
    publish_Year=forms.IntegerField()
    pages=forms.IntegerField()
