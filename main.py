import sys


from rootpath import Rootpath
from report_data import MapReport
from report_data import Report
from report_name import ReportName

from duplicated_files import Duplicated

def main():
    opts = sys.argv
    print( "The arguments are {0}".format ( str(opts) ) )
    read_files = Rootpath ( opts ).files()
    
    Report ( ReportName().all() ).write(read_files) 
   
    duplicated = Duplicated(read_files).files()
    
    MapReport ( Report ( ReportName().duplicated() )) .write   (  duplicated     )
    
if __name__ == "__main__":
    main()
