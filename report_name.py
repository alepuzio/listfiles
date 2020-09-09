import sys
import os
import datetime
#import settings

class ReportName:

    def __init__(self):
        self.extension = "csv"
        self.DATE_FORMAT="%Y-%m-%d"

    def unique(self):
        '''@return the name of final report file of the files (once written)'''
        return "{0}{1}.{2}".format("unique", datetime.datetime.now().strftime(self.DATE_FORMAT), self.extension )

    def duplicated(self):
        '''@return the name of final report file of the duplicated files'''
        return "{0}{1}.{2}".format("duplicated", datetime.datetime.now().strftime(self.DATE_FORMAT), self.extension )

    def all(self):
        '''@return the name of final report file'''
        return "{0}{1}.{2}".format("All", datetime.datetime.now().strftime(self.DATE_FORMAT), self.extension )
