serve:
	python manage.py runserver

migrations:
	python manage.py makemigrations
	python manage.py migrate

superuser:
	python manage.py createsuperuser

requirements:
	python -m pip install -r requirements.txt

test:
	python manage.py test

flush:
	python manage.py flush

rmmigrations:
	rm -rfv ./*/migrations/!(__init__.py)

syncdb:
	python manage.py migrate --run-syncdb

showmigrations:
	python manage.py showmigrations