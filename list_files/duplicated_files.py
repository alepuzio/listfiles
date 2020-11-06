#import sys
#sys.path.append('../physical')
from .single_file import SingleFile
from tests.test_duplicated_files import Occurrence
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
"""
class Occurrence:
    @overview: class about the occurence of the file'
    def __init__(self, new_map_files, new_file_tmp):
        self.map_files = new_map_files
        self.file_tmp = new_file_tmp

    def excessive(self):
        return 1 < len (self.list_files()) #TODO remove magic number

    def list_files(self):
        list_files = [k for k,v in self.map_files.items() if v == self.file_tmp ] 
        return list_files 
"""
