PYTHON=$(shell which python3)

serve: build
	@cd docs && mdbook serve -n 0.0.0.0 -p 3000

context:
	@cd docs && $(PYTHON) ../scripts/CollectCommunityMods.py

build: context
	@cd docs && mdbook build
