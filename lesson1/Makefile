.PHONY: help
help:
		@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: setup
setup: ## installing conda virtualenv and install poetry in that enviroment
		pip install --upgrade pip
		pip install poetry

.PHONY: build
build: ## build image
	docker build . -t "backend:$$(poetry version -s)"

.PHONY: start-db
start-db: ## start db
	docker run --name mongo -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin-user -e MONGO_INITDB_ROOT_PASSWORD=admin-password -v mongo-volume:/data/db -d mongo:latest

.PHONY: stop-db
stop-db: ## stop db
	docker rm -f mongo

.PHONY: deploy
deploy: start-db ## deploy
	docker run -d --rm -p 8000:8000 -v "$${PWD}"/backend:/app:ro --name backend "backend:$$(poetry version -s)"

.PHONY: stop
stop: stop-db ## stop
	docker rm -f backend
