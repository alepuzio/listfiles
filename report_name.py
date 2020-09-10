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
        return "report_unique-{0}.{1}".format( self.time(), self.extension )

    def duplicated(self):
        '''@return the name of final report file of the duplicated files'''
        return "report_duplicated-{0}.{1}".format( self.time(), self.extension )

    def all(self):
        '''@return the name of final report file'''
        return "report_all-{0}.{1}".format( self.time(), self.extension )

    
    def time(self):
        return  datetime.datetime.now().strftime(self.DATE_FORMAT)
