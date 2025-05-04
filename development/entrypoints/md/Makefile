.DEFAULT_GOAL := help

SHELL := /bin/bash

help: ## show help message
	# command from: https://gist.github.com/prwhite/8168133
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[$$()% a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


clear: ## clear all cache and pyc files
	cd ../../../components/databases/md/schemes/md/ &&\
		rm -rf .pytest_cache htmlcov  &&\
		find . -name "*.egg-info" -exec rm -rf {} \; &&\
		find . -name "*.pyc" -exec rm -f {} \;


venv-init:  ## remove old and create new virtual env, install package req
	rm -rf venv && python3.13 -m venv venv
	source venv/bin/activate  &&\
		python --version &&\
		pip install --upgrade pip &&\
		cd ../../../components/databases/md/schemes/md/ &&\
		pip install -e .[dev]

run-tests:  ## run tests
	source venv/bin/activate &&\
		set -a &&\
 		source ../../.env &&\
 		source .env &&\
 		set +a &&\
 		cd ../../../components/databases/md/schemes/md/ &&\
 		pytest tests


lint:  ## ruff check src tests
	source venv/bin/activate &&\
		cd ../../../components/databases/md/schemes/md/ &&\
		ruff check src tests

lint-autofix:  ## fix ruff E501, next fix ruff
	source venv/bin/activate &&\
		cd ../../../components/databases/md/schemes/md/ &&\
		yapf -irp src tests &&\
		ruff check src tests --fix


alembic-upgrade-heads:  ## database alembic upgrade heads
	source venv/bin/activate &&\
		set -a &&\
 		source ../../.env &&\
 		source .env &&\
 		set +a &&\
 		cd ../../../components/databases/md/schemes/md/ &&\
 		python -m db.md.md.entrypoints.alembic upgrade heads

