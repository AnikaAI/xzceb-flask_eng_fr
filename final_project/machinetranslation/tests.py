import unittest

from translator import englishToFrench, frenchToEnglish

# class TestEnglishToFrenchEmpty(unittest.TestCase): 
#     def test1(self): 
#         self.assertEqual(englishToFrench(""), "") 


class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(""), "") 
        self.assertEqual(englishToFrench("Hello"), "Bonjour") 
        self.assertNotEqual(englishToFrench("Bonjour"), "Hello")  

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish(""), "") 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") 
        self.assertNotEqual(frenchToEnglish("Hello"), "Bonjour")

unittest.main()
