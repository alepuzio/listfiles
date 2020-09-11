import os
import time
import datetime
import unittest
from single_file import SingleFile


class RowCSV:
    '''@overview: class that manage the data as CSV row'''
    def __init__(self, new_single_file):
        self.single_file = new_single_file

    def data(self):#TODO what is annotation @property
        filename = ";".join (( self.single_file.name().name() , self.single_file.directory(), self.single_file.name().extension() ) ) 
        return self.csv(filename)

    def time(self):
        return datetime.datetime.fromtimestamp ( float(self.single_file.timestamp () ) ).strftime( "%Y-%m-%d-%H-%M" ) 
        
    def csv(self, filename):
        data  = (filename , str( self.single_file.dimension () ), self.time(), "\n")
        return ";".join ( data ) #TODO move in a decorator

        
class RowDuplicated:

    def __init__(self, new_origin):
        self.origin = new_origin

    def data(self):
        filename = "{0}{1}{2}.{3}".format(self.origin.single_file.directory(), os.sep, self.origin.single_file.name().name(), self.origin.single_file.name().extension() ) 
        return self.origin.csv( filename )
