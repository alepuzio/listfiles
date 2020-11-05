import sys
sys.path.append('../logical')
from  duplicated_files import Occurrence

#class TestOccurrence(unittest.TestCase):
    

def test_excessive_OK ( ) :
    fileTmp = "file_1.txt"
    mapFile = {
        "singlefile_file_1.txt":"file_1.txt", 
        "singlefile_dati_interni_diversi_file_1.txt":"file_1.txt", 
        "singlefile_file_2.txt":"file_2.txt" 
    }

    result = Occurrence(mapFile, fileTmp).excessive()
    assert True == result

def test_listFiles_OK ( ) :
    fileTmp = "file_1.txt"
    mapFile = {
        "singlefile_file_1.txt":"file_1.txt", 
        "singlefile_dati_interni_diversi_file_1.txt":"file_1.txt", 
        "singlefile_file_2.txt":"file_2.txt" 
        }
    result = Occurrence(mapFile, fileTmp).listFiles() 
    expected = [ "singlefile_file_1.txt", "singlefile_dati_interni_diversi_file_1.txt"]
    assert result == expected
