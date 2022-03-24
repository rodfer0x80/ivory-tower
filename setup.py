from setuptools import setup
from setuptools import find_packages


setup(
    name='automatic_couscous',
    version='0.0.0',
    description='deploying scanners with no effort',
    author='trevalkov',
    author_email='trevalkov@protonmail.com',
    url='https://github.com/trevalkov/ivory-tower',
    packages=find_packages(exclude=('tests*', 'testing*')),
    py_modules=['configs'],
    entry_points={
        'console_scripts': [
            'mainpy = main.main:main',
            'testpy = test.test:test',
        ]
    }
    )
