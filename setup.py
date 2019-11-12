from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["numpy>=1.17"]

setup(
    name="growingdifgrow-trial",
    version="0.0.1",
    author="Christopher Konow",
    author_email="chriskonow27@gmail.com",
    description="Runs simulations of differential growth Turing pattern formation, with growing domain",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://https://github.com/chrisk27/growingdifgrow-trial",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
)