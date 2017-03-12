.PHONY: setup install install-dev clean test run

.venv:
	virtualenv -p python3 .venv

setup: .venv
	echo "Virtual Environment Created"

install: setup
	./.venv/bin/pip install -r requirements.txt

install-dev: setup
	./.venv/bin/pip install -r requirements-dev.txt

run: install
	PYTHONPATH=./ ./.venv/bin/smtpd -n -c smtp2api.handler -l :2525 -d

test: install-dev
	./.venv/bin/py.test

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
