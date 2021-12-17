SHELL:= /bin/bash

install:
	poetry install

synth: install
	poetry run cdk synth

deploy: install
	poetry run cdk deploy --all

destroy: install
	poetry run cdk destroy --all
