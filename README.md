# DjangoTemplate

**Env**
- VsCode
- Python 3.9
- Django 3.2.3

**Init**
1. django-admin startproject web_project
2. python manage.py migrate
3. python manage.py createsuperuser

**Create An App**
1. python manage.py startapp hello
2. add functions in views.py
3. create url.py in hello
4. add path("", include("hello.urls")) in web_project/urls.py
5. add hello to INSTALLED_APPS in web_project/settings.py


**Add Models to App**
1. add class to your model
2. python manage.py makemigrations hello
3. python manage.py migrate
4. add class to hello/admin.py(optional, for display)


**Add Views to App**
1. (optional) add html template to your template/
2. (optional) add paths of templates to your TEMPLATES in setting.py
3. add class to your view.py
4. add router to your hello/urls.py
5. add class to hello/admin.py(optional, for display)

**RUN**
python manage.py runserver