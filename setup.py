from setuptools import setup
# https://packaging.python.org/distributing/#configuring-your-project

setup(

    # using pip-tools
    # list main required packages
    # run pip-compile to get them into a fancy annotated requirements.txt
    install_requires=[
        'flask',
        'tinydb',
        'randomcolor'
    ]
)

