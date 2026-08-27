.PHONY: install install-cloc scan scan-docs ask

# Create/update venv only when requirements.txt changes
venv/bin/activate: requirements.txt
	python3 -m venv .venv
	./.venv/bin/pip install --upgrade pip
	./.venv/bin/pip install -r requirements.txt
	touch .venv/bin/activate

install: venv/bin/activate install-cloc

install-cloc:
	@which cloc > /dev/null || (echo "Installing cloc..." && \
		if [ "$$(uname)" = "Darwin" ]; then \
			brew install cloc; \
		else \
			sudo apt-get update && sudo apt-get install -y cloc; \
		fi)

scan-docs: venv/bin/activate
	./.venv/bin/python main.py scan /Users/zsolt.bea/Repos