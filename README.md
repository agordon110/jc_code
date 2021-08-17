# Code Challenge
# Requirements
• macOS

• python 2 *Default macOS install or python 3 with Homebrew*
# Usage
Change to script directory

To run the demo script

	python run_Action.py

To run unittest framework tests

	python test_Action.py_

# Design Decisions
Chose to not accept any arbitrary actions and chose to create an allow list in the Action object.

addAction only records new actions. Chose to have the calculations generated in the getStats method

# Testing
Basic testing using python unittest framework.
Linting using flake8