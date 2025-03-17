import sys
import os
import unittest
from unittest.mock import patch # import proper absolute import and testing libraries.

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.parser import LSystemParser # import class to test.

class TestParser(unittest.TestCase):
    def setUp(self): # create an instance of LSystemParser before every test.
        self.axiom = "F"
        self.rules = {"F": "F+F--F+F"}
        self.iterations = 2
        self.obj = LSystemParser(self.axiom, self.rules, self.iterations)
        
    def tearDown(self): # delete the instance of LSystemParser after each test.
        del self.obj

class TestParse(TestParser):
    def test_valid_zero_iterations(self): # check zero iterations returning the axiom unchanged.
        parser = LSystemParser(self.axiom, self.rules, 0)
        result = parser.parse()
        self.assertEqual(result, "F")
        
    def test_valid_one_iteration(self): # check one iteration.
        parser = LSystemParser(self.axiom, self.rules, 1)
        result = parser.parse()
        self.assertEqual(result, "F+F--F+F")
        
    def test_valid_two_iterations(self): # check two iterations.
        result = self.obj.parse()
        expected = "F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F"
        self.assertEqual(result, expected)
        
    def test_valid_three_iterations(self): # check three iterations.
        parser = LSystemParser(self.axiom, self.rules, 3)
        result = parser.parse()
        self.assertTrue(result.startswith("F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F+"))
        self.assertEqual(len(result), 148)
        
    def test_valid_complex_rules(self): # check a simple axiom with complex rules.
        axiom = "A"
        rules = {"A": "AB", "B": "A"}
        parser = LSystemParser(axiom, rules, 5)
        result = parser.parse()
        self.assertEqual(result, "ABAABABAABAAB")
        
    def test_valid_mixed_characters(self): # check an axiom with special characters.
        axiom = "F-G"
        rules = {"F": "F+G", "G": "F-G"}
        parser = LSystemParser(axiom, rules, 1)
        result = parser.parse()
        self.assertEqual(result, "F+G-F-G")
        
    def test_valid_unchanged_characters(self): # check an axiom that keeps a variable unchanged.
        axiom = "F+G"
        rules = {"F": "FF"}
        parser = LSystemParser(axiom, rules, 2)
        result = parser.parse()
        self.assertEqual(result, "FFFF+G")
        
    def test_valid_empty_axiom(self): # check an empty axiom.
        parser = LSystemParser("", self.rules, 3)
        result = parser.parse()
        self.assertEqual(result, "")
        
    def test_valid_empty_rules(self): # check empty rules leading to the axiom unchanged.
        parser = LSystemParser(self.axiom, {}, 3)
        result = parser.parse()
        self.assertEqual(result, "F")

    def test_valid_branching(self): # check branching by asserting the number of brackets in the result to be the same.
        axiom = "X"
        rules = {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"}
        parser = LSystemParser(axiom, rules, 3)
        result = parser.parse()
        self.assertTrue("[" in result and "]" in result)  
        self.assertTrue(result.count("[") == result.count("]"))  
        
    def test_invalid_nonetype_iterations(self): # test with None in iterations raising an error. 
        parser = LSystemParser(self.axiom, self.rules, None)
        with self.assertRaises(TypeError):
            parser.parse()

if __name__ == "__main__":
    unittest.main()