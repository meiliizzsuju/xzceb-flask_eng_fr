import unittest

from translator import frenchToEnglish, englishToFrench

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertEqual(frenchToEnglish(''),'Text is null')
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertEqual(englishToFrench(''),'Text is null')
        self.assertEqual(englishToFrench('Hello'),'Bonjour')


unittest.main()