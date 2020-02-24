import os

from setuptools import find_packages
from setuptools import setup

version = '0.1a.dev'

install_requires = [
    ]

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-flakes',
    'pytest-pep8',
    ]

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst'), encoding='utf-8').read()
except IOError:
    README = ''


setup(name='pyproject',
      version=version,
      description='pyproject package template',
      long_description=README,
      url='https://github.com/dnouri/pyproject',
      author='Daniel Nouri',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require={
          'testing': tests_require,
          'all': tests_require,
          },
      entry_points={
          'console_scripts': [
              # Create a script called myscript that will call
              # function 'cli' from the 'main' module:

              # 'myscript = pyproject.main:cli',
              ],
          },
      )
