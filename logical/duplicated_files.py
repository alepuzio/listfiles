from physical.single_file import SingleFile
import unittest

class Duplicated:
    
    '''TODO refactoring'''

    def __init__(self, new_list_files):
        self.list_files = new_list_files

    def files(self):
        '''@return the map<SingleFile, list_of_files_duplicated'''
        map_files =  {}
        for file_tmp in self.list_files:
            map_files[file_tmp] = file_tmp.name().name() 
        duplicated = {}
        for filename_tmp in set(map_files.values()) : 
            number_occurrences = Occurrence (map_files, filename_tmp ) 
            if number_occurrences.excessive(): 
                duplicated [filename_tmp] = number_occurrences.list_files()
        #at the end of the cycle
        return duplicated

class Occurrence:
    '''@overview: class about the occurence of the file'''
    def __init__(self, new_map_files, new_file_tmp):
        self.map_files = new_map_files
        self.file_tmp = new_file_tmp

    def excessive(self):
        return 1 < len (self.list_files()) #TODO remove magic number

    def list_files(self):
        list_files = [k for k,v in self.map_files.items() if v == self.file_tmp ] 
        return list_files 

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
