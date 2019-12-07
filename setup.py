import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DansonGo 5", # Replace with your own username
    version="0.0.2",
    author="Gen Li",
    author_email="gen.li@yale.edu",
    description="A simple module for generating a bunch of SOPs for different schools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gen-li/SOP_GEN",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
