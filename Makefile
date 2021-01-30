lint:
	poetry run flake8 difference_calculator
	
test:
	pytest difference_calculator/test/test_comprasion.py
