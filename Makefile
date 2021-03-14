lint:
	poetry run flake8 gendiff
	
test:
	pytest --junit-xml test_result
