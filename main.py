import sys
import os
import datetime
import settings
import message

from SingleFile import SingleFile

from rootpath import Rootpath
from report import Report
from report_name import ReportName

def main():
    opts = sys.argv
    print(message.ARGUMENTS + str(opts))
    read_files = Rootpath ( opts ).files()
    
    unique_read_files = []
    duplicated_read_files = []
    
    for file_tmp in read_files:
        print("cycle({0})".format( file_tmp.filename() ) )
        if file_tmp in unique_read_files:
            duplicated_read_files.append ( file_tmp)
        else:
            unique_read_files.append ( file_tmp)
        
    duplicated = Report ( ReportName().duplicated() , duplicated_read_files)
    duplicated.write()

    unique = Report ( ReportName().unique() , unique_read_files )
    unique.write()

if __name__ == "__main__":
    main()
