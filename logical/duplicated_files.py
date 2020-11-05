import sys
sys.path.append('../physical')
from single_file import SingleFile
import unittest

class Duplicated:
    
    '''TODO refactoring'''

    def __init__(self, newListFiles):
        self.listFiles = newListFiles

    def files(self):
        '''@return the map<SingleFile, list_of_files_duplicated'''
        mapFiles =  {}
        for fileTmp in self.listFiles:
            map_files[fileTmp] = fileTmp.name().name() 
        duplicated = {}
        for filenameTmp in set(mapFiles.values()) : 
            numberOccurrences = Occurrence (mapFiles, filenameTmp ) 
            if numberOccurrences.excessive(): 
                duplicated [filenameTmp] = numberOccurrences.listFiles()
        #at the end of the cycle
        return duplicated

class Occurrence:
    '''
    @overview: class about the occurence of the file
    '''
    def __init__(self, newMapFiles, newFileTmp):
        self.mapFiles = newMapFiles
        self.fileTmp = newFileTmp

    def excessive(self):
        '''
        @return TRUE if there's more than 1 file in the list of files
        '''
        return 1 < len (self.listFiles()) #TODO remove magic number

    def listFiles(self):
        '''
        @return the list of the files mapped by the file self.newFileTmp
        '''
        listFiles = [k for k,v in self.mapFiles.items() if v == self.fileTmp ] 
        return listFiles 

