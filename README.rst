======================
cookiecutter-pypackage
======================

* Required packages are not hardcoded in the ``setup.py`` file. All the required packages are inside the ``requirements`` folder.

* Package requirements are broken down into separate files::

.. code:: bash

    ├── requirements
    │   ├── dev.txt
    │   ├── prod.txt
    │   ├── test.txt

* Creates a default class based on the package name.

* Vanilla testing setup with `unittest` and `python setup.py test`
* Travis-CI_: Ready for Travis Continuous Integration testing
* Bumpversion: Pre-configured version bumping with a single command


Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/flatspace/cookiecutter-pypackage.git

About the package ``requirements``:

* Install the dev requirements in your local machine by running::

    pip install -r requirements/dev.txt

* Requirements for Unit testing (on Travis) can be found in ``requirements/test.txt``

* Requirements for Prod build can be found in ``requirements/prod.txt``

* Prod requirements are reused in both Dev and Test requirements.

Then:

* Create a repo and put it there.
* Add the repo to your Travis CI account.
* Run the script `travis_pypi_setup.py` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
* Release your package the standard Python way. Here's a release checklist:
  https://gist.github.com/audreyr/5990987
* (Optional) If you feel like pinning the requirements for your package, you can
  add a `requirements.txt` that specifies packages and version numbers.
