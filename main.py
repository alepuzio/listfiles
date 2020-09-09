import sys
import os
import datetime
#import settings
#import message

from SingleFile import SingleFile

from collections import Counter
from rootpath import Rootpath
from report import Report
from report_name import ReportName

def main():
    opts = sys.argv
    print( "The arguments are {0}".format ( str(opts) ) )
    read_files = Rootpath ( opts ).files()
    
    Report ( ReportName().all() , read_files ).write()
    
    map_files =  {}
    for file_tmp in read_files:
        map_files[file_tmp] = file_tmp.name().name() 
    print ("map:{0}".format( str (map_files) ) )
    duplicated = {}
    for filename_tmp in  map_files.values(): 

        value = Counter(map_files.values()) [filename_tmp] 
        if 1 < value:
            print(  filename_tmp + "->"+  str( value ) ) 
            duplicated [filename_tmp] = [k for k,v in map_files.items() if v == filename_tmp ]
            print("duplicated: " + str ( duplicated ) )

    MapReport ( ReportName().duplicated() , duplicated).write()
    '''
    unique_read_files = []
    duplicated_read_files = []
    for file_tmp in read_files:
        print("unique file {0} ".format( str( unique_read_files ) ) ) 
        if file_tmp.name() in unique_read_files[file_tmp]:
            duplicated_read_files.append ( file_tmp)
            print("duplicated file {0} in {1}".format( file_tmp.name(), str (unique_read_files) ) )
        else:
            unique_read_files.append ( file_tmp)
        
    Report ( ReportName().duplicated() , duplicated_read_files).write()

    Report ( ReportName().unique() , unique_read_files ).write()
    '''

if __name__ == "__main__":
    main()
