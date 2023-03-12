.PHONY: show-params init destroy clean clean-pyc clean-build clean-test
	create-environment delete-environment pip-upgrade sort-requirements
	requirements pre-commit-install pre-commit-uninstall lint
	new-problem help

###############################################################################
# GLOBALS                                                                     #
###############################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME := $(shell basename $(subst -,_,$(PROJECT_DIR)))
ENVIRONMENT_NAME = $(PROJECT_NAME)
PYTHON_INTERPRETER = python3
PIP_INTERPRETER = pip
PYTHON_VERSION = 3.9
PIP_VERSION = 22.3

# --- REQUIREMENTS-RELATED
REQUIREMENTS_FILE = $(PROJECT_DIR)/requirements.txt
REQUIREMENTS_FILE_TEMP = $(PROJECT_DIR)/requirements.tmp
REQUIREMENTS_DEV_FILE = $(PROJECT_DIR)/requirements-dev.txt
REQUIREMENTS_DEV_FILE_TEMP = $(PROJECT_DIR)/requirements-dev.tmp

# ----------------------------- Python-specific -------------------------------
# - Checking what type of python one is using
# Anaconda
ifeq (,$(shell which conda))
HAS_CONDA=False
else
HAS_CONDA=True
# We need to specify the following commands in order to properly activate the
# Anaconda environment.
SHELL=/bin/bash
# Note that the extra activate is needed to ensure that the activate floats env to the front of PATH
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate
CONDA_DEACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda deactivate ; conda deactivate
endif

# - Pyenv
ifeq (,$(shell which pyenv))
HAS_PYENV=False
else
HAS_PYENV=True
endif


###############################################################################
#  VARIABLES FOR COMMANDS                                                     #
###############################################################################

## Show the set of input parameters
show-params:
	@ printf "\n-------- GENERAL ---------------\n"
	@ echo "PROJECT_DIR:                       $(PROJECT_DIR)"
	@ echo "PROJECT_NAME:                      $(PROJECT_NAME)"
	@ echo "ENVIRONMENT_NAME:                  $(ENVIRONMENT_NAME)"
	@ echo "PYTHON_INTERPRETER:                $(PYTHON_INTERPRETER)"
	@ echo "PYTHON_VERSION:                    $(PYTHON_VERSION)"
	@ echo "PIP_VERSION:                       $(PIP_VERSION)"
	@ echo "REQUIREMENTS_FILE:                 $(REQUIREMENTS_FILE)"
	@ echo "REQUIREMENTS_FILE_TEMP:            $(REQUIREMENTS_FILE_TEMP)"
	@ echo "REQUIREMENTS_DEV_FILE:             $(REQUIREMENTS_DEV_FILE)"
	@ echo "REQUIREMENTS_DEV_FILE_TEMP:        $(REQUIREMENTS_DEV_FILE_TEMP)"
	@ printf "\n-------- PYTHON ---------------\n"
	@ echo "HAS_CONDA:                         $(HAS_CONDA)"
	@ echo "HAS_PYENV:                         $(HAS_PYENV)"
	@ printf "\n-------- CODING PROBLEMS ---------------\n"
	@ echo "ASSETS_DIR:                        $(ASSETS_DIR)"
	@ echo "SAMPLE_FILENAME:                   $(SAMPLE_FILENAME)"
	@ echo "SCRIPT_FILEPATH:                   $(SCRIPT_FILEPATH)"
	@ echo "COMPANY_NAME:                      $(COMPANY_NAME)"
	@ echo "PROBLE_TYPE:                       $(PROBLE_TYPE)"
	@ echo "YEAR:                              $(YEAR)"
	@ echo "TITLE:                             $(TITLE)"
	@ printf "\n--------------------------------\n"

## Initialize the repository for code development
init: clean create-envrc delete-environment create-environment
ifeq (True,$(HAS_CONDA))
	@ ($(CONDA_ACTIVATE) $(ENVIRONMENT_NAME) ; $(MAKE) requirements)
	@ printf "\n\n>>> New Conda environment created. Activate with: \n\t: conda activate $(ENVIRONMENT_NAME)"
	@ $(MAKE) show-params
	@ printf "\n\n>>> Project initialized!"
	@ ($(CONDA_ACTIVATE) $(ENVIRONMENT_NAME) ; $(MAKE) pre-commit-install )
	@ ($(CONDA_ACTIVATE) $(ENVIRONMENT_NAME) ; $(MAKE) lint )
else
	@ direnv allow || echo ""
	@ echo ">>> Continuing installation ..."
	@ $(MAKE) requirements
	@ $(MAKE) show-params
	@ printf "\n\n>>> Project initialized!\n"
	@ $(MAKE) pre-commit-install
	@ $(MAKE) lint
endif

## Remove ALL of the artifacts + Python environments
destroy: clean pre-commit-uninstall delete-environment delete-envrc
	@ echo ">>> Deleted all artifacts and environments!"

###############################################################################
# MISCELLANEOUS COMMANDS                                                      #
###############################################################################

# -------------------- Functions for cleaning repository ----------------------

## Removes artifacts from the build stage, and other common Python artifacts.
clean: clean-build clean-pyc clean-test

## Removes Python file artifacts
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

## Remove build artifacts
clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

## Remove test and coverage artifacts
clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

# ---------------------- Functions for Python environment ---------------------

## Set up the envrc file for the project.
create-envrc:
	@ echo "cat $(PROJECT_DIR)/template.envrc > $(PROJECT_DIR)/.envrc"
	@ cat $(PROJECT_DIR)/template.envrc > $(PROJECT_DIR)/.envrc

## Delete the local envrc file of the project
delete-envrc:
	@ rm -rf $(PROJECT_DIR)/.envrc || echo ""

## Creates the Python environment
create-environment:
ifeq (True,$(HAS_CONDA))
	@ echo ">>> Detected CONDA ... Creating new conda environment!"
	@ echo ">>> \tCreating environment: \t $(ENVIRONMENT_NAME)"
	@ conda create --name $(ENVIRONMENT_NAME) python=$(PYTHON_VERSION) -y  || echo ""
	@ echo ">>> New conda environment created. Activate with: \n conda activate $(ENVIRONMENT_NAME)"
else ifeq (True,$(HAS_PYENV))
	@ echo ">>> Detected PYENV ... Creating new Pyenv environment!"
	@ echo ">>> \tCreating environment: \t $(ENVIRONMENT_NAME)"
	@ pyenv virtualenv $(PYTHON_VERSION) $(ENVIRONMENT_NAME) || echo ""
	@ pyenv local $(ENVIRONMENT_NAME)
	@ echo ">>> New Pyenv environment created: '$(ENVIRONMENT_NAME)'"
	@ pyenv virtualenvs
	@ echo
endif

## Deletes the Python environment
delete-environment:
ifeq (True,$(HAS_CONDA))
	@ echo ">>> Detected CONDA ... Deleting Conda environment, if applicable!"
	@ echo ">>> Deleting environment:    '$(ENVIRONMENT_NAME)'"
	@ ($(CONDA_DEACTIVATE) ; conda env remove --name $(ENVIRONMENT_NAME) -y) || echo ""
	@ echo ">>> Conda environment deleted: '$(ENVIRONMENT_NAME)'"
else ifeq (True,$(HAS_PYENV))
	@ echo ">>> Detected PYENV ... Deleting Pyenv environment!"
	@ echo ">>> Deleting environment:    '$(ENVIRONMENT_NAME)'"
	@ pyenv uninstall -f $(ENVIRONMENT_NAME) || echo ""
	@ rm $(PROJECT_DIR)/.python-version || echo ""
	@ echo ">>> Pyenv environment deleted: '$(ENVIRONMENT_NAME)'"
	@ pyenv virtualenvs
	@ echo
endif

## Upgrade the version of the 'pip' package
pip-upgrade:
	@ $(PYTHON_INTERPRETER) -m pip install --no-cache-dir -q --upgrade pip==$(PIP_VERSION)

## Sort the project packages requirements file
sort-requirements:
	@ 	sort $(REQUIREMENTS_FILE) | grep "\S" > $(REQUIREMENTS_FILE_TEMP) && \
		mv $(REQUIREMENTS_FILE_TEMP) $(REQUIREMENTS_FILE)
	@ 	sort $(REQUIREMENTS_DEV_FILE) | grep "\S" > $(REQUIREMENTS_DEV_FILE_TEMP) && \
		mv $(REQUIREMENTS_DEV_FILE_TEMP) $(REQUIREMENTS_DEV_FILE)


## Install Python dependencies into the Python environment
requirements: pip-upgrade sort-requirements
	@ $(PYTHON_INTERPRETER) -m pip install --no-cache-dir -q -r $(REQUIREMENTS_DEV_FILE)

# -------------------------- Functions for Code Linting -----------------------

## Installing the pre-commit Git hook
pre-commit-install:
	@ pre-commit install

## Uninstall the pre-commit Git hook
pre-commit-uninstall:
	@ pre-commit uninstall || echo ""

## Run the 'pre-commit' linting step manually
lint:
	@ pre-commit run -a --hook-stage manual

###############################################################################
# CODING PROBLEMS                                                             #
###############################################################################

ASSETS_DIR = $(PROJECT_DIR)/assets
SAMPLE_FILENAME = "sample_problem.py"
SCRIPT_FILEPATH = "$(ASSETS_DIR)/create_challenge_file.py"

# Variables to use when creating new directory
COMPANY_NAME="general"
PROBLE_TYPE="general"
YEAR="2023"
TITLE=""

## Function to create a file for a new coding problem
new-problem:
	@	$(PYTHON_INTERPRETER) $(SCRIPT_FILEPATH) \
		--company "$(COMPANY_NAME)" \
		--problem-type "$(PROBLE_TYPE)" \
		--year $(YEAR) \
		--title "$(TITLE)"

###############################################################################
# Self Documenting Commands                                                   #
###############################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=25 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
