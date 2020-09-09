import os
from os.path import splitext
import time
import datetime
import settings

class SingleFile:

    def __iter__(self):
        return iter(self.name)

    def __init__(self, new_physical_data):
        self.physical = new_physical_data

    def directory(self):
        return  self.physical.path().split('.')[0]#TODO move out the method

    def dimension(self):
        return self.physical.data().st_size

    def timestamp(self):
        return self.physical.data().st_atime
    
    def extension(self):
        return  self.physical.path().split('.')[1]#TODO move out the method

    def filename(self): 
        list_subdirectory = self.physical.path().split(os.sep)
        list_subdirectory.reverse() 
        return list_subdirectory[0].split(".")[0]#TODO move out the method

    def __eq__(self, other):
        #return self.dimension() == other.dimension() and self.filename() == other.filename()
        return (self.filename() == other.filename())
    


class PhysicalData:

    def __init__(self, new_current, new_directory):
        self.directory = new_directory
        self.currentfile = new_current 
    
    def data(self): 
        path = self.path()
        filetmp  = open( path, 'r' );
        statinfo = os.stat( path )
        filetmp.close()
        return statinfo

    def path(self):
        return self.directory + os.sep + self.currentfile;

class RowCSV:

    def __init__(self, new_single_file):
        self.single_file = new_single_file

    def tocsv(self):#TODO cosa fa questa annotation
        data  = ( self.single_file.filename(),  self.single_file.extension(), 

                "\n")
            #self.single_file.directory (),  self.single_file.dimension(), "\n")
                #self.single_file.extension () , str( self.single_file.dimension () ), self.time(), "\n")
        return ";".join ( data ) 

    def time(self):
        return datetime.datetime.fromtimestamp ( float(self.single_data.timestamp () ) ).strftime(settings.DATE_FORMAT) 
        

