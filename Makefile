# run tests "make watch" or "make watch dirname"
watch:
	ptw -c --verbose --config ./pytest.ini -- --verbose --cov-config .coveragerc --cov
	# ptw -c --verbose payload -- --cov-config .coveragerc --cov=payload

test:
	ptw -c --verbose -- --verbose --cov-config .coveragerc --cov=${dir}

cleanproject:
	rm -rf `find -name "__pycache__"`
	rm -rf `find -name "*.pyc"`
	rm -rf `find -name "*cache"`
	rm -rf `find -name "*.coverage"`
	rm -rf `find -name "*.coverage.*"`

.PHONY: test
