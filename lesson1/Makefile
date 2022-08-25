.PHONY: help
help:
		@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: setup
setup: ## installing conda virtualenv and install poetry in that enviroment
		pip install --upgrade pip
		pip install poetry

.PHONY: deploy
deploy:
	docker run --rm -p 8000:8000 backend:0.1.0 uvicorn app:app --host 0.0.0.0 --reload
