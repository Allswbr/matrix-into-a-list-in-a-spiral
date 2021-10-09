from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

with open('requirements_dev.txt', "r") as requirements_file:
    requirements = requirements_file.read().splitlines()

setup(
    name="get_matrix",
    version="0.0.1",
    author="Oleg Buravtsov",
    author_email="olegburavtsov00@gmail.com",
    description="Library for unfolding a square matrix according to the snail rule counterclockwise",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Avito-2021-autumn/python-trainee-assignment",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8.9",
    ],
)