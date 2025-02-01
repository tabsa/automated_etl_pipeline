from setuptools import setup, find_packages
from dataset_etl import __version__


# Read requirements from file
def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()
    
setup(
    name="dataset_etl",
    version=__version__,
    packages=find_packages(),
    install_requires=read_requirements(),
    author="tabsa",
    author_email="tas.tiago.sousa@gmail.com",
    description="A sample ETL pipeline in python with automated release using github actions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tabsa/automated_etl_pipeline",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
