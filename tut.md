CMD
Change dir to d: 
D: 

part 1

Go to ur directory

    CREATE virtual env:

virtualenv venv

    To activate:

First locate: C:\Users\User\Py-Development\myproject

venv\Scripts\activate

    To disactivate:

venv\Scripts\deactivate.bat

Start django project:

django-admin startproject myproject

    To RUN the site:Locate the mange.py and test it by running:

python manage.py runserver

To create as imple web forum or discussion board locate manage.py and run code here:

django-admin startapp boards

Part 2 

Was facing some problem when I was doing the youtube tutorial, realized the solution is pretty 
straight forward in fact: 
uncle Urls.py: 
    path('', include('boards.urls')),



                                                DjangoGirls: 


    PART: Create Tables for models in your database 
URL: https://tutorial.djangogirls.org/en/django_models/
Error: in models.py, setting changed to settings 

CODE:   python manage.py makemigrations boards  (author used blog instead of boards)
        python manage.py migrate boards

    PART: Django ORM and QuerySets 
URL: https://tutorial.djangogirls.org/en/django_orm/


TO enter Django interactive console, go to manage.py location: 
CODE: python manage.py shell
