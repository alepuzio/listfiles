import sys
import os
import datetime
import settings
import Position
import message

from SingleFile import SingleFile
from rootpath import Rootpath

def main():
    """
        Summary line.

        It parses command line options

        Parameters
        ----------
        nil

        Returns
        -------
        nil
    """
    opts = sys.argv
    print(message.ARGUMENTS + str(opts))

    rootpath = Rootpath(opts)
    extension = buildextension(opts)
    reportname = buildreportname(opts)
    separator = buildseparator(opts)

    readdirectory(rootpath, extension, reportname, separator)



def buildseparator(opts):
    """
        It parses command line options
        opts: array    input parameters
    """
    if (opts.__len__()) > Position.SEPARATOR:
        separator = opts[ Position.SEPARATOR]
    else:
        separator = settings.DEFAULT_SEPARATOR
    return separator


def buildextension(opts):
    """
        It determines the type of file to read
        ----------
        opts: array    input parameters
    """
    if opts.__len__() > Position.EXTENSION:
        extension = opts[Position.EXTENSION].replace('.', '')
    else:
        extension = ''
    return extension


def buildreportname(opts):
    """
        It creates the name of final report file
        ----------
        opts: array    input parameters
      """
    if opts.__len__() > Position.REPORT_NAME:
        reportname = opts[Position.REPORT_NAME]
    else:
        reportname = settings.NAME_REPORT_FILE + datetime.datetime.now().strftime(settings.DATE_FORMAT) + settings.EXTENSION_FINAL_FILE
    return reportname


def readdirectory(rootpath): #TODO move in class Rootpath
    """
        It read a directory recursavely
        ----------
        rootpath: class    abolsut epath of root directory
    """
    readfiles = []
    try:
        existing_directory = os.path.exists(rootpath.data())
        if (existing_directory):
            walkdir(rootpath, readfiles)
    except:
        print (   sys.exc_info() )
    return readfiles;

def buildsinglefile(currentfile, directory):
    """
        It parses command line options
        ----------
        currentfile: file    File in reading now
        directory: file
            Abolsute path of the file
    """
    print("a1")
    x = SingleFile(currentfile, directory)
    return x

def walkdir(root_path,  readfiles ):
    """
        It traverses root directory, and list directories as dirs and files as files
        ----------
        root_path: string    root of the path
        readfiles: list            list of read files inside path
    """
    for root, dirs, files in os.walk(root_path):

        path = root.split(os.sep)

        for file1 in files:
            row = buildsinglefile(file1, os.sep.join(path))
            readfiles.append(row.tocsv)
        for directory in dirs:
            walkdir(directory, readfiles)


if __name__ == "__main__":
    main()
