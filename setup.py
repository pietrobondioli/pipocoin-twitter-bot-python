from setuptools import setup, find_packages

setup(
    name="pipocoin",
    version="0.1.0",
    author="Pietro Bondioli",
    author_email="pietrobondiolideveloper@gmail.com",
    packages=find_packages(exclude=["tests", "tests.*"]),
    test_suite="tests",
    license="MIT",
)
