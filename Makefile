test:
	python -m unittest discover -s tests -p '*_spec.py'

test-watch:
	watch -n 1 make test

run:
	python main.py

day-2:
	python day_2.py