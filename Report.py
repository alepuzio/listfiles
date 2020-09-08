import sys
import os
import datetime
import settings
import Position
import message

from SingleFile import SingleFile
from rootpath import Rootpath



class Report(opts):
    """
    """

    def __init__(self, new_name, new_list_files):
        self.name = new_name
        self.list_files = new_list_files

    def name(self):#TODO move in another class
        if opts.__len__() > Position.REPORT_NAME:
            reportname = opts[Position.REPORT_NAME]
        else:
            reportname = settings.NAME_REPORT_FILE + datetime.datetime.now().strftime(settings.DATE_FORMAT) + settings.EXTENSION_FINAL_FILE
        return reportname

    def homonym(self):
        if (os.path.exists(reportname)):
        os.remove(reportname)

    def reportrectory(rootpath, extension, reportname, separator):
        """
            It read a directory recursavely
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
        try:
            #create file
            report = open(self.name, settings.AUTHORIZATION_FILE)
            report.write(self.tocsvLabel())
            self.writerows(readfiles, report)
            report.close()
        except:
            print (  sys.exc_info()  )
        print (message.END_EXECUTION )


def tocsvLabel():
    """
        It return the summary of CSV file
    """
    return settings.SUMMARY_FINAL_FILE

def writerows (readfiles, report):
    """
        It writes the elements of list of file in target file
        ----------
        readfiles: list
            list of SingleFile in csv form
        report: file
            final file of report
    """
    for file1 in readfiles:
        report.write(file1)
    print(message.END_WRITING_FILE)
