'''
    setup file
'''
from setuptools import setup

setup(
    name='pryceless',
    version="0.1",
    package_dir={'': 'src'},
    packages=['scripts', 'templates', 'tests'],
    package_data={'': ['*.template', '*.expected']},
    include_package_data=True,
)
