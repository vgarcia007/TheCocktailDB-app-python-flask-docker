build:
	cd web && docker build --no-cache -t compose-flask .

compose: build
	docker-compose up

stop:
	docker-compose down

update:
	/bin/bash copy2container.sh

buhu:
	echo "test"