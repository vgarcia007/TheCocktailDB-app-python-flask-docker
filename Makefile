build-dev:
	cd web && docker build --no-cache -t cocktail-app-dev .

compose-dev:
	docker-compose -f docker-compose-dev.yml up -d

build-prod:
	cd web && docker build --no-cache -t cocktail-app-prod .

compose-prod:
	docker-compose up -d

update:
	docker cp web thecocktaildb-app-python-flask-docker_web_1:/
