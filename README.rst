.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org//ckanext-acl.svg?branch=master
    :target: https://travis-ci.org//ckanext-acl

.. image:: https://coveralls.io/repos//ckanext-acl/badge.svg
  :target: https://coveralls.io/r//ckanext-acl

.. image:: https://pypip.in/download/ckanext-acl/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-acl/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-acl/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-acl/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-acl/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-acl/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-acl/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-acl/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-acl/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-acl/
    :alt: License

=============
ckanext-acl
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!


Implentation of ACL for ckan.

When extension enabled, new tab `Permissions` added to admin interface.
Here you can manage user permissions on per-user level.

In order to add new managed permission, one should implement `ckanext.acl.interfaces.IACL`
and define `update_permission_list` method in plugin and change `perm` - first positional argument
passed into this method. `perms` is `ckanext.acl.access_permissions.AccessPermissions` object so
you can check available actions there.

---------------
Config Settings
---------------

Document any optional config settings here. For example::

    # The minimum number of hours to wait before re-checking a resource
    # (optional, default: 24).
    ckanext.acl.some_setting = some_default_value


------------------------
Development Installation
------------------------

To install ckanext-acl for development, activate your CKAN virtualenv and
do::

    git clone https://github.com//ckanext-acl.git
    cd ckanext-acl
    python setup.py develop
    pip install -r dev-requirements.txt
    paster acl init


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.acl --cover-inclusive --cover-erase --cover-tests


---------------------------------
Registering ckanext-acl on PyPI
---------------------------------

ckanext-acl should be availabe on PyPI as
https://pypi.python.org/pypi/ckanext-acl. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


----------------------------------------
Releasing a New Version of ckanext-acl
----------------------------------------

ckanext-acl is availabe on PyPI as https://pypi.python.org/pypi/ckanext-acl.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags
