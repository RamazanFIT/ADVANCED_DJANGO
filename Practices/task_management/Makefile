run_linters:
	@APP=$(filter-out $@,$(MAKECMDGOALS)) && \
	isort $$APP && \
	black $$APP && \
	bandit $$APP && \
	flake8 $$APP --max-line-length=99
%:
	@: