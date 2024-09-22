# Django

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It was created to help developers build web applications quickly and efficiently, taking care of much of the hassle associated with web development.

To install django
```bash
pip install django
```

To start project in current folder
```bash
django-admin startproject backend .
```

To run server
```bash
python manage.py runserver 8000
```

Now we can build an app to manage our API.
```bash
python manage.py startapp api
```

After creating the models for our project we need to add the migrations to database.
```bash
python manage.py makemigrations
python manage.py migrate
```

Also we can specify migrations for specific apps.
```bash
python manage.py makemigrations api
```

After adding our model to admin.py. We need to create a super user to see it in admin dashboard.
```bash
python manage.py createsuperuser
```

Now go to url /admin/ to see admin dashboard and edit the model we registered to admin site.
