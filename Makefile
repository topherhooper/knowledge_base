# Variables
DOCKER_COMPOSE = docker-compose
DOCKER_IMAGE = knowledge_base-app
PYTHON = python
PIP = pip

# Default target
.PHONY: all
all: help

# Help target
.PHONY: help
help:
	@echo "Usage:"
	@echo "  make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  help                Show this help message"
	@echo "  install             Install Python dependencies"
	@echo "  run                 Run the script locally"
	@echo "  docker-build        Build the Docker image"
	@echo "  docker-up           Run the Docker container"
	@echo "  docker-down         Stop the Docker container"
	@echo "  docker-shell        Build and enter the Docker container"

# Install Python dependencies
.PHONY: install
install:
	$(PIP) install -r requirements.txt

# Run the script locally
.PHONY: run
run:
	$(PYTHON) chatgpt_document_assistant.py

# Build the Docker image
.PHONY: docker-build
docker-build:
	$(DOCKER_COMPOSE) build
	docker system prune -f --filter "until=1h"

# Run the Docker container
.PHONY: docker-up
docker-up:
	$(DOCKER_COMPOSE) up

# Stop the Docker container
.PHONY: docker-down
docker-down:
	$(DOCKER_COMPOSE) down

# Build and enter the Docker container
.PHONY: docker-shell
docker-shell: docker-build
	docker run --rm -it -v $(PWD):/app -v ~/.bashrc:/root/.bashrc -w /app $(DOCKER_IMAGE) /bin/bash