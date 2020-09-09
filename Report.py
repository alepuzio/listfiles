import sys
import os
import datetime
import settings
import message

from SingleFile import SingleFile
from rootpath import Rootpath
from SingleFile import RowCSV


class Report:
    """
    """

    def __init__(self, new_report_name, new_list_files):
        self.name = new_report_name
        self.list_files = new_list_files

    def homonym(self):
        if (os.path.exists(reportname)):
            os.remove(reportname)
        else:
            pass

    def write(self):
        """
            It read a directory recursavely
            ----------
            rootpath: string        abolsut epath of root directory
            extension: string        extension of files to read
            reportname: string       name of the final report file
            separator: string        char of separator
            Returns
            -------
            nil
        """
        try:
            #create file
            report = open(self.name, settings.AUTHORIZATION_FILE)
            report.write(self.csvLabel())
            self.writerows( self.list_files, report)
            report.close()
        except:
            print (  sys.exc_info()  )
        print ("The file {0} is finally written".format ( self.name)  )


    def csvLabel(self):
        '''@return the summary of CSV file
        '''
        return settings.SUMMARY_FINAL_FILE

    def writerows (self, readfiles, report):
        """
            It writes the elements of list of file in target file
            ----------
            readfiles: list    list of SingleFile in csv form
            report: file        final file of report
        """
        for file1 in readfiles:
            report.write(RowCSV( file1 ) .tocsv())
        print("The rows are all written")
