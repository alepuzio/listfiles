import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name = 'report-files',  
     version = '0.1.0',
     author = "Alessandro Puzielli",
     author_email = "alessandro.puzielli@alepuzio.net",
     description = "It creates one files with some data about every files insidea directory (and sub), and a report abotu duplicated files",
     long_description = long_description,
     long_description_content_type = "text/markdown",
     url = "https://github.com/alepuzio/listfiles",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
