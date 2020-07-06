from setuptools import setup, find_packages


setup(
    name='pryceless',
    version="0.1",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    package_data={'': ['*.template', '*.expected']},
    include_package_data=True,
)