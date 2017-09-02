import sys
import os
import datetime
import settings
import Position
import message

from SingleFile import SingleFile


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

    rootpath = buildrootpath(opts)
    extension = buildextension(opts)
    reportname = buildreportname(opts)
    separator = buildseparator(opts)

    readdirectory(rootpath, extension, reportname, separator)

def buildrootpath(opts):
    """
        Summary line.

        It read the rootpath

        Parameters
        ----------
        opts: array
            input parameters

        Returns
        -------
        nil
    """
    if Position.PATH > len(opts):
        print(message.INPUT_PATH_MISSING)
        sys.exit(message.ERROR_PROGRAM)
    else:
        rootpath = opts[Position.PATH]

        if (not (os.path.isabs(rootpath)) or (os.path.isfile(rootpath))):
            print(message.INPUT_PATH_UNCORRECT)
            sys.exit(message.ERROR_PROGRAM)
        else:
            print()

    return rootpath


def buildseparator(opts):
    """
        Summary line.

        It parses command line options

        Parameters
        ----------
        opts: array
            input parameters

        Returns
        -------
        nil
    """
    if (opts.__len__()) > Position.SEPARATOR:
        separator = opts[ Position.SEPARATOR]
    else:
        separator = settings.DEFAULT_SEPARATOR
    return separator


def buildextension(opts):
    """
        Summary line.

        It determines the type of file to read

        Parameters
        ----------
        opts: array
            input parameters


        Returns
        -------
        nil
    """
    if opts.__len__() > Position.EXTENSION:
        extension = opts[Position.EXTENSION].replace('.', '')
    else:
        extension = ''
    return extension


def buildreportname(opts):
    """
        Summary line.

        It creates the name of final report file

        Parameters
        ----------
        opts: array
            input parameters

        Returns
        -------
        nil
      """
    if opts.__len__() > Position.REPORT_NAME:
        reportname = opts[Position.REPORT_NAME]
    else:
        reportname = settings.NAME_REPORT_FILE + datetime.datetime.now().strftime(settings.DATE_FORMAT) + settings.EXTENSION_FINAL_FILE
    return reportname


def readdirectory(rootpath, extension, reportname, separator):
    """
        Summary line.

        It read a directory recursavely

        Parameters
        ----------
        rootpath: string
            abolsut epath of root directory
        extension: string
            extension of files to read
        reportname: string
            name of the final report file
        separator: string
            char of separator

        Returns
        -------
        nil
    """
    readfiles = []
    try:
        existing_directory = os.path.exists(rootpath)
        if (existing_directory):
            walkdir(rootpath, readfiles)
        #delete existing report file

        if (os.path.exists(reportname)):
            os.remove(reportname)
        #create file
        report = open(reportname, settings.AUTHORIZATION_FILE)
        report.write(tocsvLabel())
        writerows(readfiles, report)
        report.close()
    except:
        e = sys.exc_info()
        print(e)
    print (message.END_EXECUTION )

def buildsinglefile(currentfile, directory):
    """
        Summary line.

        It parses command line options

        Parameters
        ----------
        currentfile: file
            File in reading now

        directory: file
            Abolsute path of the file
        Returns
        -------
        nil
    """
    print("a1")
    x = SingleFile(currentfile, directory)
    return x

def walkdir(root_path,  readfiles ):
    """
        Summary line.

        It traverses root directory, and list directories as dirs and files as files

        Parameters
        ----------
        root_path: string
            root of the path
        readfiles: list
            list of read files inside path
        Returns
        -------
    """
    for root, dirs, files in os.walk(root_path):

        path = root.split(os.sep)

        for file in files:
            row = buildsinglefile(file, os.sep.join(path))
            readfiles.append(row.tocsv)
        for directory in dirs:
            walkdir(directory, readfiles)

def tocsvLabel():
    """
        Summary line.

        It return the summary of CSV file

        Parameters
        ----------
        nil

        Returns
        -------
        nil
    """
    return settings.SUMMARY_FINAL_FILE

def writerows (readfiles, report):
    """
        Summary line.

        It writes the elements of list of file in target file

        Parameters
        ----------
        readfiles: list
            list of SingleFile in csv form
        report: file
            final file of report
        Returns
        -------
        nil
    """
    for file in readfiles:
        report.write(file)
    print(message.END_WRITING_FILE)

if __name__ == "__main__":
    main()