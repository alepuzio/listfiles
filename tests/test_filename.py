import os
import unittest
from os.path import splitext

from list_files.physical_data import PhysicalData
from list_files.physical_data import PhysicalDataFake



class Filename:
    """
    class about the filename of a file
    """
    def __init__(self, new_physical):
        self.physical = new_physical
    
    def name(self): 
        """
        @return the name of a file, with extension
        """
        list_subdirectory = self.prepare()
        return list_subdirectory[0]

    def __hash__(self):
        return hash(self.physical)    

    def extension(self):
        """
        @return the extension of a file
        """
        return self.prepare()[1]

    def prepare(self):
        """
        @return the couple <name, extension> of a file
        """
        list_subdirectory = self.physical.path().split(os.sep)
        list_subdirectory.reverse()
        if not "." in list_subdirectory[0]:#TODO move in a defensive decorator
            raise Exception ("The first element of the list {0} lacks of the dot, please control".format( str(list_subdirectory[0] ) ) )
        return list_subdirectory[0].split(".")
    
    def __lt__(self, other):
        return self.name() < other.name()

    def __str__(self):
        return "Filename:{0}.{1}".format(self.name(), self.extension())

    def __eq__(self, other):
        return self.name() == self.name() and self.extension() == self.extension()

    def __repr__(self):
        return "Filename.repr:{0}.{1}".format(self.name(), self.extension())

"""
Test area
"""
def test_eq():
    one = Filename ( PhysicalDataFake( "nome1.txt", "C:\\path\\") )
    two = Filename ( PhysicalDataFake( "nome1.txt", "C:\\path\\") )
    assert one == two

def test_not_eq():
    one = Filename ( PhysicalDataFake( "nome3.txt", "C:\\path\\") )
    two = Filename ( PhysicalDataFake( "nome4.txt", "C:\\path\\") )
    assert (one ==  two)


        

