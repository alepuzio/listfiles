from logical import Format;

from logical import FileName;
from logical import DefensiveReport;
from physical import Directory
from physical import Read; 
from physical import OnDisk;

import sys;


class App:
    '''main class: receiv the data from the user'''


    def __init__(self, newdirectory):
        self.directory = newdirectory;

    def printdata(self):
        print("main: ");
        print(str(self.directory));


if __name__ == "__main__":
    a = App("321");

    ##TODO put argment control
    root = Directory(sys.argv[1]);
    filereport = DefensiveReport(FileName(sys.argv[2]));
    readFiles = root.walk();
    logicals = Read(readFiles).logical();    
    OnDisk(Format(logicals), filereport.show()).print(); 
