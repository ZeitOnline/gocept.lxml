
Setup environment:

    pip install zc.buildout twine
    buildout
    bin/test

Release:

    buildout setup . sdist
    python3 -m twine upload --repository-url https://europe-west3-python.pkg.dev/zeitonline-engineering/pypi-zon/ dist/*