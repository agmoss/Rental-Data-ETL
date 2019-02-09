import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Rental-Data-ETL",
    version="0.0.1",
    author="Andrew Moss",
    author_email="agordonmoss@gmail.com",
    description="Rental listings data collection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/agmoss",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)