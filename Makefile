# ------------
# Make all actions needed for run homework from zero.
.PHONY: d-homework-i-run
d-homework-i-run:
	make d-run

# ------------
# Make all actions needed for purge homework related data.
.PHONY: d-homework-i-purge
d-homework-i-purge:
	@make d-purge

# ------------
# Just run.
.PHONY: d-run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose up --build

# ------------
# STOP service.
.PHONY: d-stop
d-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose down

# ------------
# Purge all data related with services.
.PHONY: d-purge
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose down --volumes --remove-orphans --rmi local --timeout 0




# Init environment for developer

.PHONY: init-dev

init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install

# ------------
# Run HomeWork
.PHONY: homework-i-run

homework-i-run:
	@python main.py

# ------------
# GoodBye
.PHONY: homework-i-purge

homework-i-purge:
	@echo Goodbye

# ------------
# Run tools for files from commit
.PHONY: pre-commit-run

pre-commit-run:
	@pre-commit run

# ------------
# Run tools for all from commit
.PHONY: pre-commit-run-all

pre-commit-run-all:
	@pre-commit run --all-files

.PHONY: migrations
# Make Migrations
migrations:
	@python manage.py makemigrations

.PHONY: migrate
# Migrate
migrate:
	@python manage.py migrate

.PHONY: django-i-generate-animals-i-100
# Generate 100 animals
django-i-generate-animals-i-100:
	@python manage.py generate_animals --amount 100

.PHONY: django-i-generate-contacts-i-100
# Generate 100 contacts
django-i-generate-contacts-i-100:
	@python manage.py generate_contacts --amount 100

.PHONY: django-i-generate-ALL
# Generate ALL content with amount=100
django-i-generate-ALL:
	@python manage.py generate_animals --amount 100 && \
	python manage.py generate_contacts --amount 100