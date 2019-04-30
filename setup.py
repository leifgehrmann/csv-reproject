from setuptools import setup, find_packages

setup(
    entry_points={
        'console_scripts': [
            'csv-reproject=csv_reproject.cli:cli',
        ],
    },
    name='csv-reproject',
    packages=find_packages(include=['csv_reproject'])
)
