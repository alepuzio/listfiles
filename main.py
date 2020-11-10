import sys

from list_files.duplicated import Duplicated
from list_files.rootpath import Rootpath
from list_files.report_data import MapReport
from list_files.report_data import Report
from list_files.report_name import ReportName


def main():
    opts = sys.argv
    print( "The arguments are {0}".format ( str(opts) ) )
    read_files = Rootpath ( opts ).files()

    Report ( ReportName().all() ).write(read_files) 
    MapReport ( Report ( ReportName().duplicated() )) .write   (   Duplicated(read_files).files()  )
    
if __name__ == "__main__":
    main()
