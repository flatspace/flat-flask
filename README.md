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
