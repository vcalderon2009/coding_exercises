# Job Coding Exercises

This repository is designed for practicing coding problems during
coding interviews.

- [Instructions](#instructions)

## Instructions for local development

The repository comes with a `Makefile` that contains a set of functions
used for coding practices.

The `Makefile` comes with the following set of functions:

```bash
(base) ➜  job_coding_exercises git:(main ✗ make help
Available rules:

clean                     Removes artifacts from the build stage, and other common Python artifacts.
clean-build               Remove build artifacts
clean-pyc                 Removes Python file artifacts
clean-test                Remove test and coverage artifacts
create-environment        Creates the Python environment
create-envrc              Set up the envrc file for the project.
delete-environment        Deletes the Python environment
delete-envrc              Delete the local envrc file of the project
destroy                   Remove ALL of the artifacts + Python environments
init                      Initialize the repository for code development
lint                      Run the 'pre-commit' linting step manually
pip-upgrade               Upgrade the version of the 'pip' package
pre-commit-install        Installing the pre-commit Git hook
pre-commit-uninstall      Uninstall the pre-commit Git hook
requirements              Install Python dependencies into the Python environment
show-params               Show the set of input parameters
sort-requirements         Sort the project packages requirements file
```

Each of these functions can be accessed through the `make` command at the
base directory level.
