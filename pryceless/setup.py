'''
    setup file
'''
from setuptools import setup


setup(
    name='pryceless',
    version="0.1",
    package_dir={'': 'src'},
    packages=['conf','controls','dialogs','main','main_window','scripts','templates','tests','utils'],
    package_data={'': ['*.template', '*.expected', '*.conf']},
    include_package_data=True,
)
