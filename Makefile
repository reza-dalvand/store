run-server:
	python manage.py runserver

create-user:
		python manage.py createsuperuser

migrate:
	python manage.py makemigrations
	python manage.py migrate


translate:
	django-admin compilemessages --ignore=venv
	django-admin makemessages -l fa --ignore=venv
