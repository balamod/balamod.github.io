PYTHON := $(shell which python3)
PWD := $(shell pwd)

serve: build
	@cd docs && PATH="$(PWD)/preprocessors:$(PWD)/backends:$$PATH" mdbook serve -n 0.0.0.0 -p 3000

context:
	@cd docs && $(PYTHON) ../scripts/generate_context.py

build: context
	@cd docs && PATH="$(PWD)/preprocessors:$(PWD)/backends:$$PATH" mdbook build

install-mdbook:
	@cargo install mdbook
	@cargo install mdbook-toc
	@cargo install mdbook-emojicodes
	@cargo install mdbook-admonish
	@cargo install mdbook-external-links
	@cargo install mdbook-tera
	@cargo install mdbook-classy
	@$(PYTHON) -m pip install -r requirements.txt
