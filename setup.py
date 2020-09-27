import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydbatools",
    version="0.0.1",
    author="David Fundakowski",
    author_email="dmfundakowski@gmail.com",
    description="A package for running SQL Server tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dfundako/pydbatools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
