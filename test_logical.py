import unittest;
import io;
import os;


from logical import LogicalFile;
from logical import Format;
from logical import DefensiveLogicalFile

from physical import PrepareFile


class TestDefensiveLogicalFile(unittest.TestCase):


    def test_path(self):
        fileToRead = "C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\fake-file.txt";
        prepare = PrepareFile(fileToRead);
        lf =  prepare.analize();
        logicalfile = DefensiveLogicalFile( lf );
        result = logicalfile.path();
        expected = "C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\";
        self.assertEqual(result, expected);




class TestLogicalFile(unittest.TestCase):


    def test_path(self):
        fileToRead = "C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\fake-file.txt";
        prepare = PrepareFile(fileToRead);
        logicalfile = DefensiveLogicalFile(prepare.analize());
        result = logicalfile.path();
        expected = "C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\";
        self.assertEqual(result, expected);

    
    def test_name(self):
        fileToRead = "C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\fake-file.txt";
        prepare = PrepareFile(fileToRead);
        logicalfile = prepare.analize();
        result = logicalfile.namefile();
        expected = "fake-file";
        self.assertEqual(result, expected);


    def test_extension(self):
        fileToRead = "C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\fake-file.txt";
        prepare = PrepareFile(fileToRead);
        logicalfile = prepare.analize();
        result = logicalfile.extension()
        expected = "txt";
        self.assertEqual(result, expected);

    def test_size(self):
        fileToRead = "C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\fake-file.txt";
        prepare = PrepareFile(fileToRead);
        logicalfile = prepare.analize();
        result = logicalfile.size()
        expected = 58;
        self.assertEqual(result, expected);


    def test_datetime(self):
        fileToRead = "C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\fake-file.txt";
        prepare = PrepareFile(fileToRead);
        logicalfile = prepare.analize();
        result = logicalfile.datetime();
        expected = "2020-05-29-18-28-30";
        self.assertEqual(result, expected);




class TestDefensiveLogicalFile:

    def tes_namefile ( self ) :
        fileToRead ="C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\fake-file.txt";
        prepare = PrepareFile(fileToRead);
        logicalfile = prepare.analize();
        toPrint = DefensiveLogicalFile( logicalfile);
        result = toPrint.namefile();
        expected = "fake-file;";
        self.assertEqual(result, expected);

    def tes_path(self):
        fileToRead ="C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\fake-file.txt";
        prepare = PrepareFile(fileToRead);
        logicalfile = prepare.analize();
        toPrint = DefensiveLogicalFile( logicalfile);
        result = toPrint.namefile()
        expected = "fake-file;";
        self.assertEqual(result, expected);
   
    def tes_size(self):
        fileToRead ="C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\fake-file.txt";
        prepare = PrepareFile(fileToRead);
        logicalfile = prepare.analize();
        toPrint = DefensiveLogicalFile( logicalfile);
        result = toPrint.namefile();
        expected = "fake-file;";
        self.assertEqual(result, expected);
 
    def tes_datetime(self):
        fileToRead ="C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\fake-file.txt";
        prepare = PrepareFile(fileToRead);
        logicalfile = prepare.analize();
        toPrint = DefensiveLogicalFile( logicalfile);
        result = toPrint.namefile();
        expected = "fake-file;";
        self.assertEqual(result, expected);


class TestYYYYMMDDHHMMSS:

    def test_show(self):
        fileToRead ="C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\fake-file.txt";
        prepare = PrepareFile(fileToRead);
        logicalfile = prepare.analize();
        toPrint = DefensiveLogicalFile( logicalfile);
        result = toPrint.namefile();
        expected = "fake-file;";
        self.assertEqual(result, expected);



