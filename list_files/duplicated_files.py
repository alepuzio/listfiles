from tests.test_single_file import SingleFile
from tests.test_duplicated_files import Occurrence

class Duplicated:
    """
    @overview: class with the list of files and the occurrences of the homonym files
    """

    def __init__(self, newListFiles):
        self.listFiles = newListFiles

    def files(self):
        """
        @return the map<SingleFile, list_of_files_duplicated_with_same_filename>
        """
        mapFiles =  {}
        for fileTmp in self.listFiles:
            map_files[fileTmp] = fileTmp.name().name() 
        duplicated = {}
        for filenameTmp in set(mapFiles.values()) : #TODO translate in functional programming with lambda syntax
            numberOccurrences = Occurrence (mapFiles, filenameTmp ) 
            if numberOccurrences.excessive(): 
                duplicated [filenameTmp] = numberOccurrences.listFiles()
        #at the end of the cycle
        return duplicated
