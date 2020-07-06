from setuptools.core import setup, find_packages


setup(
    name='pryceless',
    version="0.1",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    package_data={
        '': ['*.template']
    },
    test_suite='tests'
)