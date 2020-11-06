import os
import unittest
from os.path import splitext

from .physical_data import PhysicalData
from .physical_data import PhysicalDataFake


class SingleFile:

    def __iter__(self):
        return iter(self.name)

    def __lt__(self, other):
        return len(self.filename) > len(other.filename)


    def __init__(self, new_physical_data):
        self.physical = new_physical_data
        self.filename = Filename(new_physical_data)

    def directory(self):
        dirs = self.physical.path().split(os.sep)
        value =  str( os.sep.join(dirs[0:len(dirs) -1 ] ) )
        return  value

    def dimension(self):
        return self.physical.data().st_size

    def timestamp(self):
        return self.physical.data().st_atime
    
    def __hash__(self):
        return hash(self.filename)

    def name(self):
        return self.filename

    def __eq__(self, other):
        return self.name().name() == other.name().name() and self.dimension() == other.dimension()

    def __str__(self):
        return "SingleFile.str:{0};{1}|{2}".format ( self.name().name(), self.name().extension(), str(self.dimension()) )

    def __repr__(self):
        return "SingleFile.repr:{0};{1}|{2}".format ( self.name().name(), self.name().extension() , str(self.dimension() ) )

class Filename:

    def __init__(self, new_physical):
        self.physical = new_physical
    
    def name(self): 
        list_subdirectory = self.prepare()
        return list_subdirectory[0]

    def __hash__(self):
        return hash(self.physical)    

    def extension(self):
        return self.prepare()[1]

    def prepare(self):
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

class TestSingleFile (unittest.TestCase):

    def test_eq(self):
        one = SingleFile ( PhysicalDataFake( "nome.txt", "C:\\path\\") )
        two = SingleFile ( PhysicalDataFake( "nome.txt", "C:\\path\\") )
        self.assertEqual(one, two)

    def test_not_eq(self):
        one = SingleFile ( PhysicalDataFake( "nome.txt", "C:\\path\\") )
        two = SingleFile ( PhysicalDataFake( "nome1.txt", "C:\\path\\") )
        self.assertEqual(one, two)


class TestFilename (unittest.TestCase):

    def test_eq(self):
        one = Filename ( PhysicalDataFake( "nome1.txt", "C:\\path\\") )
        two = Filename ( PhysicalDataFake( "nome1.txt", "C:\\path\\") )
        print("one:" + str( one ))
        print("two:" + str(two ) )
        self.assertEqual(one, two)

    def test_not_eq(self):
        one = Filename ( PhysicalDataFake( "nome3.txt", "C:\\path\\") )
        two = Filename ( PhysicalDataFake( "nome4.txt", "C:\\path\\") )
        print("one:" + str( one ))
        print("two:" + str(two ) )
        self.assertEqual(one, two)


        

