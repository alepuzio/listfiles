import sys
import os
from SingleFile import PhysicalData
from SingleFile import SingleFile


class Rootpath:

    def __init__(self, opts):
        self.root_path = opts[1] #TODO study how to resolve the constants in Python

    def data(self):
       return str(self.root_path )

    def exists(self):
            return os.path.exists(self.data())

    def files ( self ): #TODO move in class Rootpath
        """
            It read a directory recursavely
            ----------
            rootpath: class    abolsut epath of root directory
        """
        readfiles = []
        try:
            if ( self.exists() ):
                self.dir(self.data(), readfiles)
            else:
                print ( "the directory [{0}] doesn'nt exists".format ( self.data() ) )  
        except:
            print ( sys.exc_info() )
        print ("lunghezza {0} ".format ( str( len ( readfiles )  ) ) )
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
            for file1 in files:
                readfiles.append ( SingleFile (  PhysicalData ( file1, os.sep.join ( path ) ) ) ) 
            for directory in dirs:
                self.dir(directory, readfiles)


