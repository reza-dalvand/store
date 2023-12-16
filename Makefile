run-server:
	python manage.py runserver

user:
	python manage.py createsuperuser

migrate:
	python manage.py makemigrations
	python manage.py migrate


translate:
	django-admin compilemessages --ignore=venv
	django-admin makemessages -l fa --ignore=venv


run-tests:
	python manage.py test --pattern="test_*.py" apps/tests --verbosity=1
