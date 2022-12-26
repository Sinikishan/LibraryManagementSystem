from viewBooks.models import Book
from borrowBook.models import Borrower
from datetime import date, timedelta

book1=Book(title="On Cooking: A Textbook Of Culinary Fundamentals", isbn=131713272, author="Priscilla A.", publishYear=2006, pages=253, status="Available")
book2=Book(title="E-Marketing (7th Edition)", isbn=132953447, author="Strauss Judy.", publishYear=2013, pages=426, status="Borrowed")
book3=Book(title="e-Learning by Design", isbn=470900024, author="Frank B.", publishYear=2015, pages=112, status="Borrowed")
book4=Book(title="Electric Touch", isbn=375026569, author="Paul Smith", publishYear=2021, pages=155, status="Available")
book5=Book(title="King Lear", isbn=891047920, author="William Shakespeare", publishYear=1608, pages=190, status="Available")
book6=Book(title="Tales", isbn=766204685, author="Edgar Allan Poe.", publishYear=1953, pages=325, status="Available")
book7=Book(title="One Thousand and One Nights", isbn=220610037 ,author="William Faulkner", publishYear=2017, pages=672, status="Borrowed")
book8=Book(title="The Castle", isbn=387827412, author="Franz Kafka", publishYear=2001, pages=205, status="Available")
book9=Book(title="In Search of Lost Time", isbn=869393200, author="Marcel Proust", publishYear=2011, pages=176, status="Available")
book10=Book(title="Digital Literacy: Skills & Strategies" ,isbn=402110439 ,author="Samuel F.", publishYear=2022, pages=386, status="Available")
book1.save()
book2.save()
book3.save()
book4.save()
book5.save()
book6.save()
book7.save()
book8.save()
book9.save()
book10.save()


today=date.today()
after30Days = today+ timedelta(days=30)

borrower1=Borrower(student_id=202001648, name="Talal Alaamer", email="202001648@student.polytechnic.bh", phone= 33400499, borrow_date=today.strftime("%d/%m/%Y"), return_date=after30Days.strftime("%d/%m/%Y"), isbn=132953447, title="E-Marketing (7th Edition)")
borrower2=Borrower(student_id=202246483, name="Ahmed Jamal", email="202246483@student.polytechnic.bh", phone= 33445566, borrow_date=today.strftime("%d/%m/%Y"), return_date=after30Days.strftime("%d/%m/%Y"), isbn=470900024, title="e-Learning by Design")
borrower3=Borrower(student_id=201938364, name="Jawan Ali", email="201938364@student.polytechnic.bh", phone= 33998877, borrow_date=today.strftime("%d/%m/%Y"), return_date=after30Days.strftime("%d/%m/%Y"), isbn=220610037, title="One Thousand and One Nights")
borrower1.save()
borrower2.save()
borrower3.save()
