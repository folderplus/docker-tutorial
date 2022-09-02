.PHONY: help
help:
		@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: setup
setup: ## installing conda virtualenv and install poetry in that enviroment
		pip install --upgrade pip
		pip install poetry

.PHONY: build
build:
	docker build . -t "backend:$$(poetry version -s)"

.PHONY: deploy
deploy:
	docker run -d --rm -p 8000:8000 -v "$${PWD}"/backend:/app:ro --name backend "backend:$$(poetry version -s)"

.PHONY: stop
stop:
	docker rm -f backend
