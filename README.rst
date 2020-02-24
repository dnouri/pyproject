==========================
pyproject package template
==========================

.. image:: https://circleci.com/gh/dnouri/pyproject.svg?style=svg
    :target: https://circleci.com/gh/dnouri/pyproject

Copy this to quickly set up a new Python package.  Replace any
occurrence of 'pyproject' in the source with the name of your package
and off you go.

Installation
============

Use of `virtualenv
<http://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/>`_
is recommended.

Run this command to install dependencies::

  pip install -r requirements.txt

Then install this package::

  pip install -e .

To verify your installation, run tests::

  pytest
