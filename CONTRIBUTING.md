# Contributing

Contributions are welcome. Before you submit a pull request, please read the instructions below for setting up your environment.

In addition to the code style linters PyMunin3 uses [towncrier](https://towncrier.readthedocs.io/en/stable/) for changelog management.

## Installing requirements for pre-commit hooks

```python
pip install -r requirements.txt
```

This will install the linters and towncrier.

## Code Style

PyMunin follows [Black](https://black.readthedocs.io/en/stable/) code style. In addition selected tests from [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks) are carried out. See the `.pre-commit-config.yml` for details.

For code quality we use [Flake8](https://flake8.pycqa.org/en/latest/). To allow configuration of Flake8 in `pyproject.toml` we make use of [FlakeHeaven](https://github.com/flakeheaven/flakeheaven).

## Changelog

In order to keep track of changes and provide an up to date changelog with every release, PyMunin3 uses [towncrier](https://towncrier.readthedocs.io/en/stable/). So every PR should carry a changelog entry, that will be merged into `CHANGELOG.rst` upon release.

### Create your changelog entry

It's recommended to work on a branch in your fork. To create the required file run:

```
towncrier create --edit FILENAME
```

where FILENAME is of the form *name.type*. *Type* must be one of the defined types in `pyproject.toml` [tool.towncrier] table. Most commonly it's one of bugfix or feature. *Name* is arbitrary, but it's best to use the issue/PR number for it to avoid conflicts.

In the file add a short description and reference any issues. These will be transformed into URLs. You can preview your entry with `towncrier --draft`.
