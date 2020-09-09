import sys
import os
import datetime
#import settings
#import message

from SingleFile import SingleFile

from rootpath import Rootpath
from report import Report
from report_name import ReportName

def main():
    opts = sys.argv
    print( "The arguments are {0}".format ( str(opts) ) )
    read_files = Rootpath ( opts ).files()
    
    unique_read_files = []
    duplicated_read_files = []
     
    for file_tmp in read_files:
        print("unique file {0} ".format( str( unique_read_files ) ) ) 
        if file_tmp in unique_read_files:
            duplicated_read_files.append ( file_tmp)
            print("duplicated file {0} in {1}".format( file_tmp.name(), str (unique_read_files) ) )
        else:
            unique_read_files.append ( file_tmp)
        
    Report ( ReportName().duplicated() , duplicated_read_files).write()

    Report ( ReportName().unique() , unique_read_files ).write()

    Report ( ReportName().all() , read_files ).write()

if __name__ == "__main__":
    main()
