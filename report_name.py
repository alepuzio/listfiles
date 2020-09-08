import sys
import os
import datetime
import settings

class ReportName:

    def __init__(self, opts):
        self.name1 = opts

    def name(self):
        '''@return the name of final report file'''
        return "{0}{1}{2}".format(settings.NAME_REPORT_FILE, datetime.datetime.now().strftime(settings.DATE_FORMAT), settings.EXTENSION_FINAL_FILE)


