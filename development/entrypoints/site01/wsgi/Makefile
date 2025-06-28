.DEFAULT_GOAL := help
SHELL := /bin/bash


help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  help		to print this help message"
	@echo "  venv-init 	to remove old and create new virtual env, install required packages"


venv-init:
	rm -rf venv && python3.13 -m venv venv
	source venv/bin/activate  &&\
		python --version &&\
		pip install --upgrade pip &&\
		pip install django==5.2.3 psycopg-binary==3.2.9 psycopg==3.2.9
