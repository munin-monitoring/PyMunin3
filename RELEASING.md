# How To Release

Releases are published on [PyPI](https://pypi.org/project/PyMunin3/) only at the moment. The following outlines the release process.

## Preparation

* switch to the current stable branch
* merge or cherry pick changes into stable

## Changelog

Preview what will be added to `CHANGELOG.rst` with

```
towncrier --draft
```

If satisfied merge the changes by running `towncrier` without any options. This will merge and commit changes and clean up `changelog.d/`.

You can inspect the contents of `CHANGELOG.rst` now and if all is well **commit** the changes:

```
git commit -m 'Release PyMunin3 X.Y.Z'
```

## Release

Now all changes are in. For setuptools to produce a proper release version, add a tag and **sign** it:

```
git tag -s -m 'Release PyMunin3 X.Y.Z' vX.Y.Z
```

Check the version number:

```python
python3 -m setuptools_scm
```

Build the release:

```python
python3 -m build
```

Inspect the contents of the tarball and the wheel (unzip) in `dist/` and make sure everything is in there and nothing more. If something went wrong, fix it. Don't forget to move the tag to the latest commit or the version number will be off.

Check the release files:

```python
python3 -m twine check dist/*
```

Time to push the release to PyPI:

```python
python3 -m twine upload dist/*
```

🎉 🎺 🍾
