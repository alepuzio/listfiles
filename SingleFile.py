import os
from os.path import splitext
import time
import datetime
import settings

class SingleFile:

    def __iter__(self):
        return iter(self.name)

    def __init__(self, currentfile, newdirectory):
        self.directory = newdirectory
        pathCompleto = newdirectory + os.sep + currentfile;
        filetmp  = open(pathCompleto, 'r');
        statinfo = os.stat(pathCompleto)
        filename, file_extension = currentfile.split('.')

        self.timestamp = statinfo.st_atime
        self.name = filename
        self.extension= file_extension
        self.dimension = statinfo.st_size
        filetmp.close()

    #@property
    def tocsv(self):#TODO cosa fa questa annotation
        separator_file = settings.DEFAULT_SEPARATOR
        nome = str(self.name)+separator_file+str(self.directory)+separator_file+str(self.extension)+separator_file+str(self.dimension)+separator_file\
               + datetime.datetime.fromtimestamp(float(self.timestamp)).strftime(settings.DATE_FORMAT) +"\n"
        return nome

    def filename(self):
        return self.name

    ''' 
    def __eq__(self, other):
        return "{0}{1}{2}"
        '''
