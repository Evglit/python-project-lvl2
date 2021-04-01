lint:
	poetry run flake8 gendiff

install:
	poetry install

gendiff:
	poetry run gendiff

test:
	pytest

package-install:
	poetry build
	python3 -m pip install --user dist/*.whl.

.PHONY: gendiff
