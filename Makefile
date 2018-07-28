# run tests "make watch" or "make watch dirname"
watch:
	ptw -c --verbose --config ./pytest.ini -- --verbose --cov-config .coveragerc --cov
	# ptw -c --verbose payload -- --cov-config .coveragerc --cov=payload

test:
	ptw -c --verbose -- --verbose --cov-config .coveragerc --cov=${dir}

.PHONY: test
