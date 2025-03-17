import sys
import os
import unittest
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.parser import LSystemParser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.axiom = "F"
        self.rules = {"F": "F+F--F+F"}
        self.iterations = 2
        self.obj = LSystemParser(self.axiom, self.rules, self.iterations)
        
    def tearDown(self):
        del self.obj

class TestParse(TestParser):
    def test_zero_iterations(self):
        parser = LSystemParser(self.axiom, self.rules, 0)
        result = parser.parse()
        self.assertEqual(result, "F")
        
    def test_one_iteration(self):
        parser = LSystemParser(self.axiom, self.rules, 1)
        result = parser.parse()
        self.assertEqual(result, "F+F--F+F")
        
    def test_two_iterations(self):
        result = self.obj.parse()
        expected = "F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F"
        self.assertEqual(result, expected)
        
    def test_three_iterations(self):
        parser = LSystemParser(self.axiom, self.rules, 3)
        result = parser.parse()
        self.assertTrue(result.startswith("F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F+"))
        self.assertEqual(len(result), 148)
        
    def test_complex_rules(self):
        axiom = "A"
        rules = {"A": "AB", "B": "A"}
        parser = LSystemParser(axiom, rules, 5)
        result = parser.parse()
        self.assertEqual(result, "ABAABABAABAAB")
        
    def test_mixed_characters(self):
        axiom = "F-G"
        rules = {"F": "F+G", "G": "F-G"}
        parser = LSystemParser(axiom, rules, 1)
        result = parser.parse()
        self.assertEqual(result, "F+G-F-G")
        
    def test_unchanged_characters(self):
        axiom = "F+G"
        rules = {"F": "FF"}
        parser = LSystemParser(axiom, rules, 2)
        result = parser.parse()
        self.assertEqual(result, "FFFF+G")
        
    def test_empty_axiom(self):
        parser = LSystemParser("", self.rules, 3)
        result = parser.parse()
        self.assertEqual(result, "")
        
    def test_empty_rules(self):
        parser = LSystemParser(self.axiom, {}, 3)
        result = parser.parse()
        self.assertEqual(result, "F")

    def test_branching(self):
        axiom = "X"
        rules = {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"}
        parser = LSystemParser(axiom, rules, 3)
        result = parser.parse()
        self.assertTrue("[" in result and "]" in result)  
        self.assertTrue(result.count("[") == result.count("]"))  
        
    def test_none_in_iteration(self):
        parser = LSystemParser(self.axiom, self.rules, None)
        with self.assertRaises(TypeError):
            parser.parse()
    
    def test_negative_iterations(self):
        parser = LSystemParser(self.axiom, self.rules, -1)
        result = parser.parse()
        self.assertEqual(result, self.axiom)

if __name__ == "__main__":
    unittest.main()