from setuptools import setup
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="easing_functions",
    version="1.0.4",
    packages=["easing_functions"],
    url="https://github.com/semitable/easing-functions",
    license="GPL 3.0",
    author="Filippos Christianos",
    author_email="almak72@gmail.com",
    description="A collection of the basic easing functions for python",
    long_description=long_description,
    long_description_content_type="text/markdown",

    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
    ],
)
