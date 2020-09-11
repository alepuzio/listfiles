#import os
from os.path import splitext
import time
import datetime
#import settings
import unittest




class PhysicalData:

    def __init__(self, new_current, new_directory):
        self.directory = new_directory
        self.currentfile = new_current 
    
    def data(self): 
        path = self.path()
        filetmp  = open( path, 'r' );
        statinfo = os.stat( path )
        filetmp.close()
        #print("statinfo[{0}]".format( str ( statinfo ) ) )   #'os.stat_result'>]
        return statinfo

    def path(self):
        return self.directory + os.sep + self.currentfile;

    def __hash__(self):
        return hash(self.directory) * 10 + hash (self.currentfile)

class PhysicalDataFake:

    def __init__(self, new_current, new_directory):
        self.name = new_current
        self.dir = new_directory

    def data(self): 
        return DataFake() 
        #"[os.stat_result(st_mode=33206, st_ino=15199648742420042, st_dev=1658795973, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1599579491, st_mtime=1599579491, st_ctime=1599579491)"

    def path(self):
        return "{0}_fake/{1}".format(self.dir, self.name)

class DataFake:

    def __init__(self):
        pass

    def st_mode(self):
        return 33206

    def st_ino(self):
        return 15199648742420042

    def st_dev(self):
        return 1658795973

    def st_nlink(self):
        return 1

    def st_uid(self):
        return 0

    def st_gid(self):
        return 0

    def st_size(self):
        return 0, 
    
    def st_atime(self):
        return 1599579491

    def st_mtime(self):
        return 1599579491

    def st_ctime(self):
        return 1599579491
