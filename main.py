import sys

from logical.duplicated_files import Duplicated
from physical.rootpath import Rootpath
from report.report_data import MapReport
from report.report_data import Report
from report.report_name import ReportName


def main():
    opts = sys.argv
    print( "The arguments are {0}".format ( str(opts) ) )
    read_files = Rootpath ( opts ).files()

    Report ( ReportName().all() ).write(read_files) 
    MapReport ( Report ( ReportName().duplicated() )) .write   (   Duplicated(read_files).files()  )
    
if __name__ == "__main__":
    main()
