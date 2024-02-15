python -m venv name of your project

cd name of your project
cd Scripts
cd activate
cd..

pip install django 
django-admin startproject project .
python manage.py startapp =your app

python.exe -m pip install --upgrade pip
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver

https://myaccount.google.com/apppasswords

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ypur email'
DEFAULT_FROM_EMAIL = 'ypur email'
EMAIL_HOST_PASSWORD = 'your password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
