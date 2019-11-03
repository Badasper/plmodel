#handle dev server
run:
	python plmodel/manage.py runserver localhost:8000
migrate:
	python plmodel/manage.py makemigrations
	python plmodel/manage.py migrate

# tests
watch_cov:
	ptw -c --verbose --config ./pytest.ini -- --verbose --cov-config .coveragerc --cov=plmodel

watch_cov_dir:
	ptw -c --verbose -- --verbose --cov-config .coveragerc --cov=${dir}

watch:
	ptw -c --verbose -- --verbose

test:
	pytest --verbose -c ./pytest.ini

# tools for project
cleanproject:
	rm -rf `find -name "__pycache__"`
	rm -rf `find -name "*.pyc"`
	rm -rf `find -name "*cache"`
	rm -rf `find -name "*.coverage"`
	rm -rf `find -name "*.coverage.*"`

# omit bash
.PHONY: test
