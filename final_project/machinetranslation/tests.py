import unittest

from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertEqual(french_to_english(''),'Text is null')
        self.assertEqual(french_to_english('Bonjour'),'Hello')

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertEqual(english_to_french(''),'Text is null')
        self.assertEqual(english_to_french('Hello'),'Bonjour')


unittest.main()