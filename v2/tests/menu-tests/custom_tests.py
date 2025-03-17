import sys
import os
import unittest
from unittest.mock import patch # import proper absolute import and testing libraries.

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from menu.custom import LSystemCustom # import class to test.

class TestCustom(unittest.TestCase):
    def setUp(self): # create an instance of LSystemParser before every test.
        self.obj = LSystemCustom()
        self.valid_chars = self.obj.valid_chars

    def tearDown(self): # delete the instance of LSystemParser after each test.
        del self.obj

class TestValidateAxiom(TestCustom): # test the validation of the axiom.
    @patch('builtins.input', return_value=' ABCD ') # check a valid axiom with whitespace and all caps.
    def test_valid_caps(self, mock_input):
        result = self.obj.validate_axiom()
        self.assertEqual(result, 'ABCD')
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='         wxzy ') # check a valid axiom with whitespace and all lowercase.
    def test_valid_lowercase(self, mock_input):
        result = self.obj.validate_axiom()
        self.assertEqual(result, 'wxzy')
        mock_input.assert_called_once()

    @patch('builtins.input', return_value=' -[+]  ') # check a valid axiom with whitespace and all symbols.
    def test_valid_symbols(self, mock_input):
        result = self.obj.validate_axiom()
        self.assertEqual(result, '-[+]')
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='AfC[+G]-F+G-c  ') # check a valid axiom with whitespace and mixed characters.
    def def_test_valid_mixed(self, mock_input):
        result = self.obj.validate_axiom()
        self.assertEqual(result, 'AfC[+G]-F+G-c')
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='ABABABABABABABA  ') # check a valid axiom at the max length.
    def test_valid_length (self, mock_input):
        result = self.obj.validate_axiom()
        self.assertEqual(result, 'ABABABABABABABA')
        mock_input.assert_called_once()
    
    @patch('builtins.input', side_effect=['', 'Az[+']) # check empty input raising an error.
    def test_invalid_empty(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_axiom()
            self.assertEqual(result, 'Az[+')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tAxiom cannot be empty, please try again.')

    @patch('builtins.input', side_effect=['AB[CD]EFGHIJKLNO', 'z']) # check a long input raising an error.
    def test_invalid_long(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_axiom()
            self.assertEqual(result, 'z')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tAxiom cannot be longer than 15 characters, please try again.')
    
    @patch('builtins.input', side_effect=['AbC +FG ', '-']) # check axiom with a space raising an error.
    def test_invalid_spaces(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_axiom()
            self.assertEqual(result, '-')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tAxiom cannot contain spaces, please try again.')

    @patch('builtins.input', side_effect=['AbCF,', '[]']) # check axiom with a comma raising an error.
    def test_invalid_characters_comma(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_axiom()
            self.assertEqual(result, '[]')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with(f'\tAxiom cannot contain invalid characters. Valid characters are: {self.valid_chars}, please try again.')

    @patch('builtins.input', side_effect=['ABC(+F)', '                  c']) # check axiom with a parenthesis raising an error.
    def test_invalid_characters_parentheses(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_axiom()
            self.assertEqual(result, 'c')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with(f'\tAxiom cannot contain invalid characters. Valid characters are: {self.valid_chars}, please try again.')

    @patch('builtins.input', side_effect=['AP2', 'AB']) # check axiom with a number raising an error.
    def test_invalid_characters_number(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_axiom()
            self.assertEqual(result, 'AB')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with(f'\tAxiom cannot contain invalid characters. Valid characters are: {self.valid_chars}, please try again.')

    @patch('builtins.input', side_effect=['ABcd+_', 'AB']) # check axiom with a special character raising an error.
    def test_invalid_characters_special(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_axiom()
            self.assertEqual(result, 'AB')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with(f'\tAxiom cannot contain invalid characters. Valid characters are: {self.valid_chars}, please try again.')

class TestValidateIterations(TestCustom): # test the validation of the number of iterations. 
    @patch('builtins.input', return_value=' 2     ') # check a valid low number of iterations.
    def test_valid_low(self, mock_input):
        result = self.obj.validate_iterations()
        self.assertEqual(result, 2)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='   6    ') # check a valid mid number of iterations.
    def test_valid_mid(self, mock_input):
        result = self.obj.validate_iterations()
        self.assertEqual(result, 6)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value=' 8  ') # check a valid high number of iterations.
    def test_valid_high(self, mock_input):
        result = self.obj.validate_iterations()
        self.assertEqual(result, 8)
        mock_input.assert_called_once()
        
    @patch('builtins.input', return_value='0') # check the lowest number of iterations.
    def test_valid_lower_edge(self, mock_input):
        result = self.obj.validate_iterations()
        self.assertEqual(result, 0)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='10') # check the highest number of iterations.
    def test_valid_lower_edge(self, mock_input):
        result = self.obj.validate_iterations()
        self.assertEqual(result, 10)
        mock_input.assert_called_once()

    @patch('builtins.input', side_effect=['-1', '4']) # check the highest possible negative number of iterations raising an error.
    def test_invalid_negative_low(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 4)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations cannot be negative, please try again.')
    
    @patch('builtins.input', side_effect=['-20', '7']) # check a lower negative number of iterations raising an error.
    def test_invalid_negative_high(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 7)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations cannot be negative, please try again.')

    @patch('builtins.input', side_effect=['11', '5']) # check a lower possible high number of iterations raising an error.
    def test_invalid_large_low(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 5)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations cannot exceed 10, please try again.')

    @patch('builtins.input', side_effect=['25', '1']) # check a higher possible high number of iterations raising an error.
    def test_invalid_large_high(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 1)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations cannot exceed 10, please try again.')

    @patch('builtins.input', side_effect=[' ', '9']) # check an empty input raising an error.
    def test_invalid_empty(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 9)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations must be a valid integer, please try again.')

    @patch('builtins.input', side_effect=['3.0', '3']) # check an invalid format raising an error.
    def test_invalid_float(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 3)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations must be a valid integer, please try again.')

    @patch('builtins.input', side_effect=['5,', '5']) # check an invalid character raising an error.
    def test_invalid_character_comma(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 5)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations must be a valid integer, please try again.')

    @patch('builtins.input', side_effect=['5 iterations', '5']) # check an invalid word raising an error.
    def test_invalid_word(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 5)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations must be a valid integer, please try again.')

class TestValidateTurnAngle(TestCustom): # test the validation of the turn angle. 
    @patch('builtins.input', return_value=' 0     ') # check the lowest possible turn angle as an integer. 
    def test_valid_low_int(self, mock_input):
        result = self.obj.validate_turn_angle()
        self.assertEqual(result, 0.0)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='         360.0   ') # check the highest possible turn angle as an integer.
    def test_valid_high_int(self, mock_input):
        result = self.obj.validate_turn_angle()
        self.assertEqual(result, 360.0)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='0.06     ') # check a small float. 
    def test_valid_low_float(self, mock_input):
        result = self.obj.validate_turn_angle()
        self.assertEqual(result, 0.06)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='359.78  ') # check a high float.
    def test_valid_high_float(self, mock_input):
        result = self.obj.validate_turn_angle()
        self.assertEqual(result, 359.78)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='267.78567563756') # check a long float.
    def test_valid_long(self, mock_input):
        result = self.obj.validate_turn_angle()
        self.assertEqual(result, 267.78567563756)
        mock_input.assert_called_once()

    @patch('builtins.input', side_effect=['-1', '100']) # check the lowest possible negative integer raising an error.
    def test_invalid_negative_int(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\t\n\tYour turn angle must be between 0° and 360°, please try again.')
    
    @patch('builtins.input', side_effect=['361', '100']) # check the highest possible positive integer raising an error.
    def test_invalid_positive_int(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\t\n\tYour turn angle must be between 0° and 360°, please try again.')
    
    @patch('builtins.input', side_effect=['-0.09', '100']) # check a small float raising an error.
    def test_invalid_negative_float(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\t\n\tYour turn angle must be between 0° and 360°, please try again.')
    
    @patch('builtins.input', side_effect=['360.000001', '100']) # check a large float raising an error.
    def test_invalid_positive_float(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\t\n\tYour turn angle must be between 0° and 360°, please try again.')
    
    @patch('builtins.input', side_effect=[' ', '100']) # check an empty input raising an error.
    def test_invalid_empty(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour turn angle must be a valid floating-point number, please try again.')

    @patch('builtins.input', side_effect=['56,7', '100']) # check a comma raising an error.
    def test_invalid_comma(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour turn angle must be a valid floating-point number, please try again.')

    @patch('builtins.input', side_effect=['57°', '100']) # check a degree raising an error.
    def test_invalid_degree(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour turn angle must be a valid floating-point number, please try again.')

    @patch('builtins.input', side_effect=['100 degrees', '100']) # check a word raising an error.
    def test_invalid_letter(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour turn angle must be a valid floating-point number, please try again.')

class TestValidateStartingDirection(TestCustom): # test the validation of the starting direction, same as for the turn angle.
    @patch('builtins.input', return_value=' 0     ') 
    def test_valid_low_int(self, mock_input): 
        result = self.obj.validate_starting_direction()
        self.assertEqual(result, 0.0)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='         360.0   ')
    def test_valid_high_int(self, mock_input):
        result = self.obj.validate_starting_direction()
        self.assertEqual(result, 360.0)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='0.06     ')
    def test_valid_low_float(self, mock_input):
        result = self.obj.validate_starting_direction()
        self.assertEqual(result, 0.06)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='359.78  ')
    def test_valid_high_float(self, mock_input):
        result = self.obj.validate_starting_direction()
        self.assertEqual(result, 359.78)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='267.78567563756')
    def test_valid_long(self, mock_input):
        result = self.obj.validate_starting_direction()
        self.assertEqual(result, 267.78567563756)
        mock_input.assert_called_once()

    @patch('builtins.input', side_effect=['-1', '100'])
    def test_invalid_negative_int(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_starting_direction()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\t\n\tYour starting direction must be between 0° and 360°, please try again.')
    
    @patch('builtins.input', side_effect=['361', '100'])
    def test_invalid_positive_int(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_starting_direction()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\t\n\tYour starting direction must be between 0° and 360°, please try again.')
    
    @patch('builtins.input', side_effect=['-0.09', '100'])
    def test_invalid_negative_float(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_starting_direction()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\t\n\tYour starting direction must be between 0° and 360°, please try again.')
    
    @patch('builtins.input', side_effect=['360.000001', '100'])
    def test_invalid_positive_float(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_starting_direction()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\t\n\tYour starting direction must be between 0° and 360°, please try again.')
    
    @patch('builtins.input', side_effect=[' ', '100'])
    def test_invalid_empty(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_starting_direction()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour starting direction must be a valid floating-point number, please try again.')

    @patch('builtins.input', side_effect=['56,7', '100'])
    def test_invalid_character(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_starting_direction()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour starting direction must be a valid floating-point number, please try again.')

    @patch('builtins.input', side_effect=['57°', '100'])
    def test_invalid_character(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_starting_direction()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour starting direction must be a valid floating-point number, please try again.')

    @patch('builtins.input', side_effect=['100 degrees', '100'])
    def test_invalid_letter(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_starting_direction()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour starting direction must be a valid floating-point number, please try again.')

if __name__ == "__main__":
    unittest.main()