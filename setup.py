
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="listfiles", # Replace with your own username
    version="0.0.1",
    author="Alessandro Puzielli aka alepuzio",
    author_email="alessandro.puzielli@alepuzio.net",
    description="My software to build a report of file inside a directory",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alepuzio/listfiles",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
