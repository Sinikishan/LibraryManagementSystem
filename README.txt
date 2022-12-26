# LibraryManagementSystem

- Author: Talal Alaamer
- Date: 26/12/2022
- This is a university project for the course "Web Development with NoSQL".

# Content
A library management system website has been created using the Django framework. The main functionalities for this website are:
- Ability to add new books
- Ability to view the list of existing books and their details
- Ability to borrow books

# Website Components
- Front-end: HTML, CSS, Javascript, Bootstrap
- Back-end: Python, MongoDB, Django

# Software needed to run the project
- Anaconda Prompt
- Python
- MongoDB

# Steps to run the project
1. Download or clone this repository.
2. Launch the anaconda prompt
3. Change the directory to the project's directory
4. Perform the following commands:
  - conda create --name LMS django ///// Creates a new virtual environment called LMS /////
  - conda activate LMS ///// Activates the newly created virtual environment /////
  - pip install -r requirements.txt ///// Installs additional files to help run this project universally with different versions of django /////
  - python manage.py makemigrations ///// Makes migrations in case of any changes in models /////
  - python manage.py migrate ///// Migrates everything to the database /////
  - python manage.py shell < mongoSetup.py ///// Generates a sample list of data to be viewed on the website /////
  - python manage.py createsuperuser ///// Create a website user in order to use all website functionalities /////
  - python manage.py runserver ///// Start the server /////
5. Paste this host http://127.0.0.1:8000/ to your url bar and access the website!

#Video demonstration of the website and django code
Link: 
