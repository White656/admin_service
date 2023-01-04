start-dev:
	docker-compose up -d
build-dev:
	docker-compose up -d --build
logs:
	docker-compose logs -f
stop:
	docker-compose stop
kill:
	docker-compose kill
clear:
	docker system prune -a
lsof_get:
	sudo lsof -i :5432
isort-src:
	isort .
auto-pep:
	autopep8 --in-place --recursive ./example_usage
make-message:
	python admin_panel/manage.py makemessages -l en -l ru
compile-message:
	python admin_panel/manage.py compilemessages -l en -l ru
