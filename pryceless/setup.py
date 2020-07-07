from setuptools import setup, find_packages


setup(
    name='pryceless',
    version="0.1",
    package_dir={'': 'src'},
    packages=['scripts', 'templates'],
    package_data={'': ['*.template', '*.expected']},
    include_package_data=True,
)