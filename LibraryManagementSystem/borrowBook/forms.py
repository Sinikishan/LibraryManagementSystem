from django import forms

class BorrowForm(forms.Form):
    student_id=forms.IntegerField()
    name=forms.CharField()
    email=forms.EmailField()
    phone=forms.IntegerField()
