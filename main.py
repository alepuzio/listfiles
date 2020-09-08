import sys
import os
import datetime
import settings
import Position
import message

from SingleFile import SingleFile

from rootpath import Rootpath
from report_name import ReportName

def main():
    opts = sys.argv
    print(message.ARGUMENTS + str(opts))

    rootpath = Rootpath(opts)
    reportname = ReportName(opts).name()

    read_files = readdirectory(rootpath)
    #TODO flag -d :find duplicates
    for file_tmp in read_files:
        print("cycle({0})".format( file_tmp ) )


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
            walkdir(rootpath.data(), readfiles)
    except:
        print (   sys.exc_info() )
    return readfiles;


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
            row = SingleFile(file1, os.sep.join(path))
            readfiles.append(row.tocsv)
        for directory in dirs:
            walkdir(directory, readfiles)


if __name__ == "__main__":
    main()
