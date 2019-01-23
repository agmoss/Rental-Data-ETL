import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Rental_Analytics_App",
    version="0.0.1",
    author="Andrew Moss",
    author_email="agordonmoss@gmail.com",
    description="A web app for rental property analytis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/agmoss/Rental_Analytics_App",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)