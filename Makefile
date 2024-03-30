PYTHON=$(shell which python3)

serve:
	$(MAKE) build
	mdbook serve -n 0.0.0.0 -p 3000

build:
	@cd docs
	@$(PYTHON) docs/scripts/CollectCommunityMods.py
	@mdbook build
	@cd -
