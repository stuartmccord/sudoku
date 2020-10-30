import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="sudoku",
    version="1.0.0",
    description="Basic library to solve sudoku",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/stuartmccord/sudoku",
    author="Stuart McCord",
    author_email="stuart.mccord@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["sudoku"],
    include_package_data=True,
)