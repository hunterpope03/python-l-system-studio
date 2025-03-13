import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.parser import l_system_parser # import function to test

class TestLSystemParser(unittest.TestCase):
    """
    Tests the l_system_parser function. 

    Tests for simple and complex axioms, rules, and iterations.

    Note: Automatic validation of user inputs will occur in the modules.py file. This ensures all invalid inputs that would otherwise cause the l_system_parser function to fail are caught.
    """

    def test_simple_parse(self): 
        """
        Test basic functionality.
        """
        axiom = 'F+f'
        rules = {'F': 'FXf', 'X': 'F'}
        iterations = 3
        parsed = l_system_parser(axiom, rules, iterations)
        self.assertEqual(parsed, 'FXfFfFXff+f')

    def test_parse_with_complex_axiom(self):
        axiom = 'F+F-f[G]-XF'
        rules = {'F': 'F-G', 'X': 'F'}
        iterations = 3
        parsed = l_system_parser(axiom, rules, iterations)
        self.assertEqual(parsed, 'F-G-G-G+F-G-G-G-f[G]-F-G-GF-G-G-G')
        
    def test_parse_with_empty_rules(self):
        axiom = 'F+X'
        rules = {}
        iterations = 5
        parsed = l_system_parser(axiom, rules, iterations)
        self.assertEqual(parsed, 'F+X')
    
    def test_parse_with_complex_rules(self): 
        axiom = 'F+X'
        rules = {'F' : 'X+F-[f+X]', 'X' : 'F-X', 'f' : 'G'}
        iterations = 3
        parsed = l_system_parser(axiom, rules, iterations)
        self.assertEqual(parsed, 'X+F-[f+X]-F-X+F-X+X+F-[f+X]-[G+F-X]-[G+X+F-[f+X]-F-X]+F-X+X+F-[f+X]-[G+F-X]-X+F-[f+X]-F-X')

    def test_parse_with_no_iterations(self):
        axiom = 'F-X+G'
        rules = {'F' : 'F-G[X]', 'G' : 'F+X'}
        iterations = 0
        parsed = l_system_parser(axiom, rules, iterations)
        self.assertEqual(parsed, 'F-X+G')

    def test_parse_with_many_iterations(self):
        axiom = 'F'
        rules = {'F' : 'F+X', 'X' : 'F[G]'}
        iterations = 9
        parsed = l_system_parser(axiom, rules, iterations)
        self.assertEqual(parsed, 'F+X+F[G]+F+X[G]+F+X+F[G][G]+F+X+F[G]+F+X[G][G]+F+X+F[G]+F+X[G]+F+X+F[G][G][G]+F+X+F[G]+F+X[G]+F+X+F[G][G]+F+X+F[G]+F+X[G][G][G]+F+X+F[G]+F+X[G]+F+X+F[G][G]+F+X+F[G]+F+X[G][G]+F+X+F[G]+F+X[G]+F+X+F[G][G][G][G]+F+X+F[G]+F+X[G]+F+X+F[G][G]+F+X+F[G]+F+X[G][G]+F+X+F[G]+F+X[G]+F+X+F[G][G][G]+F+X+F[G]+F+X[G]+F+X+F[G][G]+F+X+F[G]+F+X[G][G][G][G]')

if __name__ == '__main__':
    unittest.main()
