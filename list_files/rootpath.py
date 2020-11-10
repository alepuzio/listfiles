import sys
import os
from tests.test_single_file import PhysicalData
from tests.test_single_file import SingleFile


class Rootpath:
    """
    @overvieww: class of the absolute path of root directory
    """
    def __init__(self, opts):
        self.root_path = opts[1] #TODO study how to resolve the constants in Python

    def data(self):
       return str(self.root_path )

    def exists(self):
        return os.path.exists(self.data())

    def files ( self ): #TODO move in class Rootpath
        """
        It read a directory recursavely
        """
        readfiles = []
        try:
            if ( self.exists() ):
                self.dir(self.data(), readfiles)
            else:
                print ( "The directory [{0}] doesn'nt exists".format ( self.data() ) )  
        except:
            print ( sys.exc_info() )
        print ("The total number of the read files is {0}".format ( str( len ( readfiles )  ) ) )
        return readfiles;


    def dir(self, root_path,  readfiles ):
        """
            It traverses root directory, and list directories as dirs and files as files
            ----------
            root_path: string    root of the path
            readfiles: list            list of read files inside path
        """
        for root, dirs, files in os.walk(root_path) :
            path = root.split(os.sep)
            for fileTmp in files:
                readfiles.append ( SingleFile (  PhysicalData ( fileTmp, os.sep.join ( path ) ) ) ) 
            for directory in dirs:
                if "." not in directory:#TODO transform in decorator
                    self.dir(directory, readfiles)
                else:
                    pass



