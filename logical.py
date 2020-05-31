
import os
from os.path import splitext
import time



class DefensiveLogicalFile:
    '''control the logicalFile contruction'''
    def __init__ (self, neworigin):
        self.origin = neworigin;

    def namefile ( self ) :
        res = ["unknown-filename", "unkown-extension"]; 
        if "." in self.origin.fileToRead.name :
            res = self.origin.namefile();
        else:
            raise Exception( "Unreadable file" + self.origin.fileToRead.name );
        return res; 

    def path(self):
        return self.origin.path() ;
    
    def size(self):
        return self.origin.size() ;
   
    def datetime(self):
        datetimeformat = YYYYMMDDHHMMSS ( self.origin.datetime() );
        res =  datetimeformat.show(); 
        return res;
    
    def extension(self):
        return self.origin.extension() ;

class YYYYMMDDHHMMSS:

    def __init__(self, newdatetime):
        self.datetime = newdatetime;

    def show(self):
        ''' show the datetiem formatted 
        as yyyy-mm-dd-hh24-mm-ss '''
        year, month, day, hour, minute, second = time.localtime(self.datetime)[:-3]
        res = ("%02d-%02d-%d-%02d-%02d-%02d" %(year, month, day, hour, minute, second))
        return res

class LogicalFile:
    '''logical representation of a file,
    no reference to filesystem propert
    filetmp.close()
    '''

    def __init__ (self, newFile, newpath, newstatinfo):
        self.fileToRead = newFile;
        self.pathToRead = newpath;
        self.statinfo = newstatinfo;

    def path(self):
        '''path of the file'''
        completepath =  os.path.abspath(self.pathToRead);
        path = (os.sep).join(completepath.split(os.sep)[0 : -1]) + os.sep;
        return path;

    def namefile (self):
        '''return the name of the file, without extension, dot and path
        the file has be named as filename.extension '''
        print (  self.fileToRead.name.split('\.'));
        filename, file_extension = self.file_with_extension();
        namefile = filename.split(os.sep);
        return namefile[-1];

    def extension(self):
        '''extension of the file: 3 letter after last dot'''
        filename, file_extension = self.file_with_extension();
        return file_extension;

    def size(self):
        ''' size of the file in byte''' 
        return self.statinfo.st_size;

    def datetime(self):
        '''date time of the file'''
        return self.statinfo.st_atime;

    ##############TODO: private method to put in another class
    def file_with_extension (self):
        filename, file_extension =  ["unknown-filename", "unkown-extension"]; 
        if  2 == len ( self.fileToRead.name.split('.')):
            filename, file_extension = self.fileToRead.name.split('.');
        return filename, file_extension;

    def stat(self):
        statinfo = os.stat(self.fileToRead);
        return statinfo;

class Format:
    ''' class that format the passed
    list of LogicalFile'''

    def __init__(self, newSetLogicalFile):
        self.setLogicalFiles = newSetLogicalFile;

    def csv(self):
        '''return the self.setLogicalFile
         as a set of Logical file formatted in CSV style'''
        res = [];
        for element in self.setLogicalFiles:
            res.append ( element.path() + str(";") + element.namefile() + ";" + str(element.size()) + ";" + str(element.datetime()));
        return res;
                

class DefensiveReport:

    def __init__(self, newfilename):
        self.origin = newfilename;

    def show(self):
        '''control if the filename is correct for report file'''
        filename = self.origin.filename; 
        if not (".txt" in filename):
            raise Exception("The filename of the report has to have the extension .txt")
        else:
            return filename;

class FileName:

    def __init__(self, newfilename):
        self.filename = newfilename;

    def show(self):
        return self.filename; 

