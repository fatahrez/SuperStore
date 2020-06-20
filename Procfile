release: python manage.py makemigrations store
release: python manage.py migrate

web: gunicorn superstore.wsgi --log-file -

