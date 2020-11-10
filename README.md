## WARNING

This project has the same functionality of my project [reportFile](https://github.com/alepuzio/reportFile).
So, any other updated of this project is postponed until either the project will be joined.


# ListFiles
--------
This application build tow report file, by passing an absolute or relative path:
- report CSV with all the files inside the directory. The data are: 
 -- path
 -- name of the file
 -- dimension in byte
 -- extension
 -- date of creation or last update

- report with all the files and, for every of these, a table with the data of the (probable) duplicates. The data are: 
-- complete path
-- dimsione in byte
-- date fo creation of last update

## Features

### Future
- Write a report with some filter in input (e.g. only files with a particural extension, only files after a date etc)
- Write a report with all the documents or images or video 
- Change the name and url of the Github repository
- Show the directories with no elements 

### Next
- Fix the style of the files and the classes as [PEP8] (https://www.python.org/dev/peps/pep-0008/)

### Running
- Write the file of _Contributing_ as [this] ( https://gist.github.com/PurpleBooth/b24679402957c63ec426/forks)

### Past
- agganciato a travis
- la directory ha lo stesso nome dell'applicazione, non src
- mettere in directory src le classi senza unit test
- spostare le classi nei file di test, così da avere accoppiamento


## Status CI Integration
 
 I use [Travis](https://travis-ci.org/)
 [![Build Status](https://travis-ci.org/alepuzio/listfiles.svg?branch=master)](https://travis-ci.org/alepuzio/list-files)

## Getting started

### Prerequisites

- Python 3.0+
- pip
- pytest 

### Installing

- Clone the project with _git-clone_ (or download directly it)
- Have fun!


## Running the tests

 - I use __unitest__ framework . I reserve a __test__ for the integration test
 - Every unit test is declared inside the class, because for me test and implementation musto go together (highly coupled)

### Break down into to end to end tests

No indications

	
### Coding styles sheets

Please read the file [CONTRIBUTING.md](http://github.com/alepuzio/listfiles/CONTRIBUTING.md)

## Deployment
 
 - Package in PypI 
 - Run    __>>> python Main.py $PATH_OF_ROOT_DIRECTORY_
 
### Built with:

- [ViM](http://www.vim.org) - one of the best text editor I know
- [unittest](https://docs.python.org/3/library/unittest.html) - most famous library about the unit testing in Python

## Contributing

Please read the [Contributing.md](http://github.com/alepuzio/listfiles/CONTRIBUTING.md) for the details about the code of conduct and the process for submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

- --Alessandro Puzielli-- - -creator- - [Alepuzio](https://github.com/alepuzio)

See also the list of [contributors](https://github.com/alepuzio/listfiles/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- --PurpleBooth-- - to publish an [excellent template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) of README that I used in this project 
- --Yegor256-- - to write the post [Elegant READMEs](https://www.yegor256.com/2019/04/23/elegant-readme.html) about the README file and the [An Open Code Base Is Not Yet an Open Source Project](https://www.yegor256.com/2018/05/08/open-source-attributes.html) for the Open Source projects

