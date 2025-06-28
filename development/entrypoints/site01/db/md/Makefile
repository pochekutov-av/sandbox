.DEFAULT_GOAL := help
.PHONY: help clean venv-init test test-cc lint lint-fix create-all migrate-upgrade-heads

SHELL := /bin/bash

PACKAGE_DIR := ../../../../../components/db/md/
PACKAGE_MODULE := db.md
ENV_MAIN_FILE := ../../../../.env


help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  help		to print this help message"
	@echo "  help-a	to print venv activate shell comands"
	@echo "  clean		to clean all cache and pyc files"
	@echo "  venv-init 	to remove old and create new virtual env, install required packages"
	@echo "  test		to run tests"
	@echo "  test-unit	to run only unit tests"
	@echo "  test-cc	to run tests with code coverage html report"
	@echo "  lint		to run linters"
	@echo "  lint-fix	to run linters with fix"
	@echo "  create-tables	to create tables (use with empty db)"
	@echo "  create-routines	to create routines"
	@echo "  loaddata	to load initial data (use with empty tables)"
	@echo "  migrate-upgrade-heads to alemic upgrade heads"
	@echo "  tune-django to create tables for use with django apps"
	@echo "  loaddata-django to load initial data for django tables"


help-a:
	@echo "source venv/bin/activate && set -a && source $(ENV_MAIN_FILE) && source .env && set +a && cd $(PACKAGE_DIR)"


clean:
	cd $(PACKAGE_DIR) &&\
		rm -rf .pytest_cache htmlcov .coverage  &&\
		find . -name "*.egg-info" -exec rm -rf {} \; &&\
		find . -name "*.pyc" -exec rm -f {} \;


venv-init:
	rm -rf venv && python3.13 -m venv venv
	source venv/bin/activate  &&\
		python --version &&\
		pip install --upgrade pip &&\
		cd $(PACKAGE_DIR) &&\
		pip install -e .[dev]


test:
	source venv/bin/activate &&\
		set -a && source $(ENV_MAIN_FILE) && source .env && set +a &&\
 		cd $(PACKAGE_DIR) &&\
 		pytest tests

# здесь специально не устанавливаем переменные окружения поскольку
# unit тесты должны работать без реальных БД, web серверов
test-unit:
	source venv/bin/activate &&\
 		cd $(PACKAGE_DIR) &&\
 		pytest tests/unit


test-cc:
	source venv/bin/activate &&\
		set -a && source $(ENV_MAIN_FILE) && source .env && set +a &&\
 		cd $(PACKAGE_DIR) &&\
 		pytest -p no:cacheprovider -s --cov-report=html --cov=src tests &&\
 		open htmlcov/index.html


lint:
	source venv/bin/activate &&\
		cd $(PACKAGE_DIR) &&\
		ruff check src tests


lint-fix:
	source venv/bin/activate &&\
		cd $(PACKAGE_DIR) &&\
		yapf -irp src tests &&\
		ruff check src tests --fix


create-tables:
	source venv/bin/activate &&\
		set -a && source $(ENV_MAIN_FILE) && source .env && set +a &&\
 		cd $(PACKAGE_DIR) &&\
 		python -m "$(PACKAGE_MODULE).entrypoints.create_tables"


create-routines:
	source venv/bin/activate &&\
		set -a && source $(ENV_MAIN_FILE) && source .env && set +a &&\
 		cd $(PACKAGE_DIR) &&\
 		python -m "$(PACKAGE_MODULE).entrypoints.create_routines"


loaddata:
	source venv/bin/activate &&\
		set -a && source $(ENV_MAIN_FILE) && source .env && set +a &&\
 		cd $(PACKAGE_DIR) &&\
 		python -m "$(PACKAGE_MODULE).fixtures.init.load"


migrate-upgrade-heads:
	source venv/bin/activate &&\
		set -a && source $(ENV_MAIN_FILE) && source .env && set +a &&\
 		cd $(PACKAGE_DIR) &&\
 		python -m "$(PACKAGE_MODULE).entrypoints.alembic"  upgrade heads


tune-django:
	source venv/bin/activate &&\
		set -a && source $(ENV_MAIN_FILE) && source .env && set +a &&\
 		cd $(PACKAGE_DIR) &&\
 		python -m "$(PACKAGE_MODULE).tuning.django.do"

loaddata-django:
	source venv/bin/activate &&\
		set -a && source $(ENV_MAIN_FILE) && source .env && set +a &&\
 		cd $(PACKAGE_DIR) &&\
 		python -m "$(PACKAGE_MODULE).fixtures.django.load"
