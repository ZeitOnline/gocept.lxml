
Setup environment:

    pip install zc.buildout twine
    buildout
    bin/test

Username and Password in Vault https://vault.ops.zeit.de/ui/vault/secrets/zon%2Fv1/show/devpi/index-zeit-default

Release:

    buildout setup . sdist
    env TWINE_REPOSITORY_URL=https://devpi.zeit.de/zeit/default/ TWINE_USERNAME=!REPLACE! TWINE_PASSWORD=!REPLACE! twine upload dist/*.tar.gz