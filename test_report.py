import unittest;
import io;
import os;


from logical import LogicalFile;
from logical import Format;
from logical import DefensiveLogicalFile

from physical import PrepareFile






class TestFormatter(unittest.TestCase):


    def tes_t_csv(self):
        fileToRead ="C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\fake-file.txt";
        prepare = PrepareFile(fileToRead);
        logicalfile = prepare.analize();
        listfiles = [];
        listfiles.append( logicalfile);
        toPrint = Format(listfiles);
        result = toPrint.csv();
        expected = "fake-file;";
        self.assertEqual(str(result[0]), expected);






class TestDefensiveReport:

    def test_show(self):
        fileToRead ="C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\fake-file.txt";
        prepare = PrepareFile(fileToRead);
        logicalfile = prepare.analize();
        toPrint = DefensiveLogicalFile( logicalfile);
        result = toPrint.namefile()
        expected = "fake-file;";
        self.assertEqual(result, expected);


class TestReportFileName:


    def test_show(self):
        fileToRead ="C:\\Users\\alepu\\Documents\\repo-github\\listfile\\listfiles\\resources\\fake-file.txt";
        prepare = PrepareFile(fileToRead);
        logicalfile = prepare.analize();
        toPrint = DefensiveLogicalFile( logicalfile);
        result = toPrint.namefile()
        expected = "fake-file;";
        self.assertEqual(result, expected);


