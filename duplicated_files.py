import sys
import os
import datetime

from SingleFile import SingleFile

from collections import Counter

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
            #print  ( list ( map_files.values() )  )
            list_examined_files =  [k for k,v in map_files.items() if v == filename_tmp ] 
            number_occurrences = Occurrence ( [k for k,v in map_files.items() if v == filename_tmp ] )

            print (str (number_occurrences ) )
            if number_occurrences.excessive(): 
                duplicated [filename_tmp] = list_examined_files
            return duplicated

        '''[filename_tmp]   )
        for filename_tmp in set(map_files.values()) : 
            occurrences = list( map_files.values()[filename_tmp] ) 
            number_occurrences = Occurrence( occurrences ) 
            if number_occurrences.excessive(): 
                duplicated [filename_tmp] = [k for k,v in map_files.items() if v == filename_tmp ]
        return duplicated 
        '''
class Occurrence:
    '''@overview: class about the occurence of the file'''
    def __init__(self, new_list_value):
        self.list_value = new_list_value

    def excessive(self):
        return 1 < self.number()

    def number(self):
        return len(self.list_value)
