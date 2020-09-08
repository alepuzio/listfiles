import sys
import os
import datetime
import settings

class ReportName:

    def __init__(self):
        self.extension = "csv"

    def unique(self):
        '''@return the name of final report file'''
        return "{0}{1}.{2}".format("unique", datetime.datetime.now().strftime(settings.DATE_FORMAT), self.extension )


    def duplicated(self):
        '''@return the name of final report file'''
        return "{0}{1}.{2}".format("duplicated", datetime.datetime.now().strftime(settings.DATE_FORMAT), self.extension )

