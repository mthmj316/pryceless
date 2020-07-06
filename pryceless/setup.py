from setuptools import setup, find_packages


setup(
    name='pryceless',
    version="0.1",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    package_data={
        '': ['*.template']
    },
    package_data={'templates': ['*.template']},
    include_package_data=True,
)