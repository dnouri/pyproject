Pyproject package template

.. image:: https://circleci.com/gh/dnouri/pyproject.svg?style=svg
    :target: https://circleci.com/gh/dnouri/pyproject


Installation
============

Use of `virtualenv
<http://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/>`_
is recommended.

Run this command to install dependencies::

  pip install -r requirements.txt

Then install this project::

  python setup.py dev

To verify your installation, run tests::

  py.test
