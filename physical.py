''' It has the data of a physicl directory'''
from logical import LogicalFile
from logical import DefensiveLogicalFile

import os;

class Directory:
    '''It wraps a physical directory in filesystem'''

    def __init__(self, newInputDir):
        '''It read a directory and the subdirectory
        inputDIr: complete path of the root directory'''
        self.inputDir = newInputDir;


    def walk(self):
        ''' return the list of the read file
        It traverses root directory, and list directories as dirs and files as files
        in recursive way'''
        print("Directory.walk("+str(self.inputDir)+")");
        readfiles = [];
        return self.walksubdir(self.inputDir, readfiles);
       
    def walksubdir(self, partialRoot, readfiles):
        ''' return the partial list of the files'''
        for root, dirs, files in os.walk(partialRoot):
            path = root.split(os.sep)
            for filetmp in files:
                readfiles.append(root + os.sep + filetmp);
            for directory in dirs:
                self.walksubdir(directory, readfiles)
        return readfiles;


class OnDisk:
    '''it print the list of LogicalFile in a file'''

    def __init__(self, newformat, newdestination):
        ''' newSetFiles: the content of the file, one element is one row;
        newDestination: file where the content is printed'''
        self.format = newformat;
        self.destination = newdestination;

    def print(self):
        '''save the list of LogicalFile in the file sef.destination'''
        with open(self.destination, "w") as outfile:
            listelements = self.format.csv();
            for element in listelements:
                outfile.write(element);
                outfile.write("\n");
        outfile.close()

class Read:
    '''class of the read files by the direcotry'''

    def __init__(self, newphysicalfiles):
        self.physicalfiles = newphysicalfiles;

    def print(self):
        '''only debug'''
        for element in self.physicalfiles:
            print(str(element));

    def logical(self):
        '''trasnfrom file in logical File'''
        res = [];
        for element in self.physicalfiles:
            analize = PrepareFile(element);
            res.append(analize.analize());
        return res;


class PrepareFile:
    '''this class open and close the file'''

    def __init__(self, newfile):
        self.file = newfile;

    def analize(self):
        '''return the LogicalFile of the current phisical file'''
        fileToAnalize  = open(self.file, "r");
        path  =  os.path.abspath ( self.file);
        statinfo =  self.stat();
        logicalFile = DefensiveLogicalFile(LogicalFile(fileToAnalize, path, statinfo) ) ;
        fileToAnalize.close();
        return logicalFile;

    
    def size(self):
        ''' size of the file in byte''' 
        fileToAnalize  = open(self.file, "r");
        statinfo = self.stat();
        fileToAnalize.close();
        return statinfo.st_size;

    def stat(self):
       statinfo = os.stat(self.file);
       return statinfo;
