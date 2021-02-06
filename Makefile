lint:
	poetry run flake8 difference_calculator
	
test:
	pytest --junit-xml test_result
