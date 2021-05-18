# DjangoTemplate

**Env**
- VsCode
- Python 3.9
- Django 3.2.3

**Init**
1. django-admin startproject web_project
2. python manage.py migrate
3. python manage.py createsuperuser

**Create App**
1. python manage.py startapp hello
2. add functions in views.py
3. create url.py in hello
4. add path("", include("hello.urls")) in web_project/urls.py

**RUN**
python manage.py runserver