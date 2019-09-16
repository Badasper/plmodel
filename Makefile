# run tests "make watch" or "make watch dirname"
watch_cov:
	ptw -c --verbose --config ./pytest.ini -- --verbose --cov-config .coveragerc --cov

watch_cov_dir:
	ptw -c --verbose -- --verbose --cov-config .coveragerc --cov=${dir}

watch:
	ptw -c --verbose -- --verbose

test:
	pytest --verbose -c ./pytest.ini

cleanproject:
	rm -rf `find -name "__pycache__"`
	rm -rf `find -name "*.pyc"`
	rm -rf `find -name "*cache"`
	rm -rf `find -name "*.coverage"`
	rm -rf `find -name "*.coverage.*"`

.PHONY: test
