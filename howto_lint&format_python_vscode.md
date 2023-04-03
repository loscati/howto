# Linting and formatting with VSCODE

## Tools to install in the VENV
The Lint softwares
- `flake8`: linter for the whole python script
- `pydocstyle`: lint for the documentation (various styles are possible, my favorite is `numpy`)
- `isort`: sort imports

The formatter:
- `black`

All of these can be installed through `pip` or `conda`. In the latter case, all are available in the `conda-forge` library.

## Extensions to install
- `Python`
  - `formatting.provider = black`
  - `linting.enabled = true`
  - `linting.pycodestyle = true`
  - `linting.pycodestyle.args = --max-line-length=88`
  - `linting.lint_on_save = true`
  - regarding all path, if you leave the defaults you will use packages from the venv 
- `black formatter`
- `flake8`
  - `args`: `--ignore=W293, --ignore=W503, --ignore=D412, --ignore=D105`. This can be modify at will, I decided to use this concurrently with the settings used in the `pyge` repo.
- `isort`

## Usage
1. save a document to lint it
2. autoformat using `black` using: `ctrl + shift + p` and using `format document`
3. correct other errors by looking at the error tab (by default, in the lower part of the editor)
4. `isort` by right clicking and select `sort imports`

