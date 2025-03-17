import sys
import os
import unittest
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from menu.custom import LSystemCustom

class TestCustom(unittest.TestCase):
    def setUp(self):
        self.obj = LSystemCustom()
        self.valid_chars = self.obj.valid_chars

    def tearDown(self):
        del self.obj

class TestValidateAxiom(TestCustom):
    @patch('builtins.input', return_value=' ABCD ')
    def test_valid_caps(self, mock_input):
        result = self.obj.validate_axiom()
        self.assertEqual(result, 'ABCD')
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='         wxzy ')
    def test_valid_lowercase(self, mock_input):
        result = self.obj.validate_axiom()
        self.assertEqual(result, 'wxzy')
        mock_input.assert_called_once()

    @patch('builtins.input', return_value=' -[+]  ')
    def test_valid_symbols(self, mock_input):
        result = self.obj.validate_axiom()
        self.assertEqual(result, '-[+]')
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='AfC[+G]-F+G-c  ')
    def def_test_valid_mixed(self, mock_input):
        result = self.obj.validate_axiom()
        self.assertEqual(result, 'AfC[+G]-F+G-c')
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='ABABABABABABABA  ')
    def test_valid_length (self, mock_input):
        result = self.obj.validate_axiom()
        self.assertEqual(result, 'ABABABABABABABA')
        mock_input.assert_called_once()
    
    @patch('builtins.input', side_effect=['', 'Az[+'])
    def test_invalid_empty(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_axiom()
            self.assertEqual(result, 'Az[+')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tAxiom cannot be empty, please try again.')

    @patch('builtins.input', side_effect=['AB[CD]EFGHIJKLNO', 'z'])
    def test_invalid_long(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_axiom()
            self.assertEqual(result, 'z')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tAxiom cannot be longer than 15 characters, please try again.')
    
    @patch('builtins.input', side_effect=['AbC +FG ', '-'])
    def test_invalid_spaces(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_axiom()
            self.assertEqual(result, '-')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tAxiom cannot contain spaces, please try again.')

    @patch('builtins.input', side_effect=['AbCF,', '[]'])
    def test_invalid_characters_comma(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_axiom()
            self.assertEqual(result, '[]')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with(f'\tAxiom cannot contain invalid characters. Valid characters are: {self.valid_chars}, please try again.')

    @patch('builtins.input', side_effect=['ABC(+F)', '                  c'])
    def test_invalid_characters_parentheses(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_axiom()
            self.assertEqual(result, 'c')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with(f'\tAxiom cannot contain invalid characters. Valid characters are: {self.valid_chars}, please try again.')

    @patch('builtins.input', side_effect=['AP2', 'AB'])
    def test_invalid_characters_number(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_axiom()
            self.assertEqual(result, 'AB')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with(f'\tAxiom cannot contain invalid characters. Valid characters are: {self.valid_chars}, please try again.')

    @patch('builtins.input', side_effect=['ABcd+_', 'AB'])
    def test_invalid_characters_special(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_axiom()
            self.assertEqual(result, 'AB')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with(f'\tAxiom cannot contain invalid characters. Valid characters are: {self.valid_chars}, please try again.')

class TestValidateIterations(TestCustom):
    @patch('builtins.input', return_value=' 2     ')
    def test_valid_low(self, mock_input):
        result = self.obj.validate_iterations()
        self.assertEqual(result, 2)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='   6    ')
    def test_valid_mid(self, mock_input):
        result = self.obj.validate_iterations()
        self.assertEqual(result, 6)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value=' 8  ')
    def test_valid_high(self, mock_input):
        result = self.obj.validate_iterations()
        self.assertEqual(result, 8)
        mock_input.assert_called_once()
        
    @patch('builtins.input', return_value='0')
    def test_valid_lower_edge(self, mock_input):
        result = self.obj.validate_iterations()
        self.assertEqual(result, 0)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='10')
    def test_valid_lower_edge(self, mock_input):
        result = self.obj.validate_iterations()
        self.assertEqual(result, 10)
        mock_input.assert_called_once()

    @patch('builtins.input', side_effect=['-1', '4'])
    def test_invalid_negative_low(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 4)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations cannot be negative, please try again.')
    
    @patch('builtins.input', side_effect=['-20', '7'])
    def test_invalid_negative_high(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 7)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations cannot be negative, please try again.')

    @patch('builtins.input', side_effect=['11', '5'])
    def test_invalid_large_low(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 5)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations cannot exceed 10, please try again.')

    @patch('builtins.input', side_effect=['25', '1'])
    def test_invalid_large_high(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 1)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations cannot exceed 10, please try again.')

    @patch('builtins.input', side_effect=[' ', '9'])
    def test_invalid_empty(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 9)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations must be a valid integer, please try again.')

    @patch('builtins.input', side_effect=['3.0', '3'])
    def test_invalid_float(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 3)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations must be a valid integer, please try again.')

    @patch('builtins.input', side_effect=['5,', '5'])
    def test_invalid_character(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 5)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations must be a valid integer, please try again.')

    @patch('builtins.input', side_effect=['5 iterations', '5'])
    def test_invalid_character(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_iterations()
            self.assertEqual(result, 5)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour number of iterations must be a valid integer, please try again.')

class TestValidateTurnAngle(TestCustom):
    @patch('builtins.input', return_value=' 0     ')
    def test_valid_low_int(self, mock_input):
        result = self.obj.validate_turn_angle()
        self.assertEqual(result, 0.0)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='         360.0   ')
    def test_valid_high_int(self, mock_input):
        result = self.obj.validate_turn_angle()
        self.assertEqual(result, 360.0)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='0.06     ')
    def test_valid_low_float(self, mock_input):
        result = self.obj.validate_turn_angle()
        self.assertEqual(result, 0.06)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='359.78  ')
    def test_valid_high_float(self, mock_input):
        result = self.obj.validate_turn_angle()
        self.assertEqual(result, 359.78)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='267.78567563756')
    def test_valid_long(self, mock_input):
        result = self.obj.validate_turn_angle()
        self.assertEqual(result, 267.78567563756)
        mock_input.assert_called_once()

    @patch('builtins.input', side_effect=['-1', '100'])
    def test_invalid_negative_int(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\t\n\tYour turn angle must be between 0° and 360°, please try again.')
    
    @patch('builtins.input', side_effect=['361', '100'])
    def test_invalid_positive_int(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\t\n\tYour turn angle must be between 0° and 360°, please try again.')
    
    @patch('builtins.input', side_effect=['-0.09', '100'])
    def test_invalid_negative_float(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\t\n\tYour turn angle must be between 0° and 360°, please try again.')
    
    @patch('builtins.input', side_effect=['360.000001', '100'])
    def test_invalid_positive_float(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\t\n\tYour turn angle must be between 0° and 360°, please try again.')
    
    @patch('builtins.input', side_effect=[' ', '100'])
    def test_invalid_empty(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour turn angle must be a valid floating-point number, please try again.')

    @patch('builtins.input', side_effect=['56,7', '100'])
    def test_invalid_character(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour turn angle must be a valid floating-point number, please try again.')

    @patch('builtins.input', side_effect=['57°', '100'])
    def test_invalid_character(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour turn angle must be a valid floating-point number, please try again.')

    @patch('builtins.input', side_effect=['100 degrees', '100'])
    def test_invalid_letter(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_turn_angle()
            self.assertEqual(result, 100)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\tYour turn angle must be a valid floating-point number, please try again.')

class TestValidateStartingDirection(TestCustom):
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