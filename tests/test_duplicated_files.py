import sys
#from  test.tesduplicated_files import Occurrence


class Occurrence:
    '''@overview: class about the occurence of the file'''
    def __init__(self, new_map_files, new_file_tmp):
        self.map_files = new_map_files
        self.file_tmp = new_file_tmp

    def excessive(self):
        #print("Occurrence.excessive")
        return 1 < len (self.list_files()) #TODO remove magic number

    def list_files(self):
        #print("Occurrence.list_files")
        list_files = [k for k,v in self.map_files.items() if v == self.file_tmp ] 
        return list_files 

def test_excessive():
    file_tmp = "file_1.txt"
    map_file = {
        "singlefile_file_1.txt":"file_1.txt", 
        "singlefile_dati_interni_diversi_file_1.txt":"file_1.txt", 
        "singlefile_file_2.txt":"file_2.txt" 
    }
    result = Occurrence(map_file, file_tmp).excessive()
    assert True == result

def test_list_files():
    file_tmp = "file_1.txt"
    map_file = {
        "singlefile_file_1.txt":"file_1.txt", 
        "singlefile_dati_interni_diversi_file_1.txt":"file_1.txt", 
        "singlefile_file_2.txt":"file_2.txt" 
    }
    result = Occurrence(map_file, file_tmp).list_files()
    expected = [ "singlefile_file_1.txt",  "singlefile_dati_interni_diversi_file_1.txt"]
    assert result == expected
