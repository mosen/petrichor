from setuptools import setup, find_packages

setup(
    name="petrichor",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'petrichor = petrichor.cli:main',
        ]
    },
    install_requires=[
        'python-jss',
        'argparse'
    ],
)
