install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 brain_games

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=brain_games --cov-report html
