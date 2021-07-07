pg:killall
release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn emergency_server.wsgi
