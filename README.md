# Code Challenge
# Requirements
• macOS

• python 2 *Default macOS install or python 3 with Homebrew*
# Usage

Make sure to run from the same directory as the scripts

To run the demo script

	python run_Action.py

To run unittest framework script

	python test_Action.py

# Design Decisions
Chose to not accept any arbitrary actions and instead opted to create an allow list in the Action object.

addAction only records new actions. Chose to have the calculations generated in the getStats method. This could easily be changeged and have the addAction method keep a dictionary of running avarages.

Maintained Camel case of addAction and getStats in case you grep for them.

# Testing
Basic testing using python unittest framework.

Linting using flake8