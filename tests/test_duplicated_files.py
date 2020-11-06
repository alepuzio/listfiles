import sys
#sys.path.insert(0, sys.path[0])
#sys.path.append('../logical')
from  list_files.duplicated_files import Occurrence
import unittest

class TestOccurrence(unittest.TestCase):
    

    def test_excessive(self):
        file_tmp = "file_1.txt"
        map_file = {
                "singlefile_file_1.txt":"file_1.txt", 
                "singlefile_dati_interni_diversi_file_1.txt":"file_1.txt", 
                "singlefile_file_2.txt":"file_2.txt" 
                }

        result = Occurrence(map_file, file_tmp).excessive()
        self.assertTrue(result)

    def test_list_files(self):
        file_tmp = "file_1.txt"
        map_file = {
                "singlefile_file_1.txt":"file_1.txt", 
                "singlefile_dati_interni_diversi_file_1.txt":"file_1.txt", 
                "singlefile_file_2.txt":"file_2.txt" 
                }
        

        result = Occurrence(map_file, file_tmp).list_files()
        expected = [ "singlefile_file_1.txt", "singlefile_file_1.txt"]
        self.assertTrue(result, expected)


    

def test_excessive():
    file_tmp = "file_1.txt"
    map_file = {
        "singlefile_file_1.txt":"file_1.txt", 
        "singlefile_dati_interni_diversi_file_1.txt":"file_1.txt", 
        "singlefile_file_2.txt":"file_2.txt" 
    }
    result = Occurrence(map_file, file_tmp).excessive()
    assert True == result

def test_list_files(self):
    file_tmp = "file_1.txt"
    map_file = {
        "singlefile_file_1.txt":"file_1.txt", 
        "singlefile_dati_interni_diversi_file_1.txt":"file_1.txt", 
        "singlefile_file_2.txt":"file_2.txt" 
    }
    result = Occurrence(map_file, file_tmp).list_files()
    expected = [ "singlefile_file_1.txt", "singlefile_file_1.txt"]
    assert result == expected
