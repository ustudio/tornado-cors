help:
	@echo '    setup ................... sets up project'
	@echo '    setup_upgrade ........... upgrades project'
	@echo '    test .................... runs tests'
	@echo '    clean ................... cleans project'
	@echo '    release ................. releases project to pypi'

setup:
	pip install -r requirements.local.txt
	pip install -r requirements.txt

setup_upgrade:
	pip install --upgrade -r requirements.local.txt
	pip install --upgrade -r requirements.txt

clean:
	@find . -name "*.pyc" -delete

test: clean
	pytest -s tests/ --junit-xml=junit.xml

release:
	python setup.py sdist register upload
