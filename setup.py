from setuptools import setup, find_packages

setup(name='treeshrink',
      version='1.1.0',
      scripts=['treeshrink.py'],
      packages= find_packages(),
      package_dir= {'treeshrink': 'treeshrink'},
      )
