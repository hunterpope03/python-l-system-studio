import sys
import os
import unittest
from unittest.mock import patch # import proper absolute import and testing libraries

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.validation import validate_menu # import class to test

class TestMenu(unittest.TestCase):
    def setUp(self): 
        self.valid_inputs = ['1', '2', '3', 'q']
        
    def tearDown(self):
        pass

class TestValidateMenu(TestMenu): # test the validation of menu inputs. 
    @patch('builtins.input', return_value='1') 
    def test_valid_input_single_digit(self, mock_input): # check a valid numeric input. 
        result = validate_menu(self.valid_inputs)
        self.assertEqual(result, '1')
        mock_input.assert_called_once()
        
    @patch('builtins.input', return_value='q') # check a valid character input.
    def test_valid_input_character(self, mock_input):
        result = validate_menu(self.valid_inputs)
        self.assertEqual(result, 'q')
        mock_input.assert_called_once()
        
    @patch('builtins.input', return_value='   2   ') # check a number with whitespace.
    def test_valid_input_with_whitespace(self, mock_input):
        result = validate_menu(self.valid_inputs)
        self.assertEqual(result, '2')
        mock_input.assert_called_once()
        
    @patch('builtins.input', side_effect=['4', '3']) # check an invalid number. 
    def test_invalid_input_then_valid(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, '3')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\nInvalid.', end=' ')
            
    @patch('builtins.input', side_effect=['', '1']) # check an empty input.
    def test_empty_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, '1')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\nInvalid.', end=' ')
            
    @patch('builtins.input', side_effect=['abc', '2']) # check a long string input. 
    def test_wrong_string_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, '2')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\nInvalid.', end=' ')
            
    @patch('builtins.input', side_effect=['Q', 'q']) # check a case sensitive input.
    def test_case_sensitive_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, 'q')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\nInvalid.', end=' ')
            
    @patch('builtins.input', side_effect=KeyboardInterrupt) # check a keyboard interrupt.
    def test_keyboard_interrupt(self, mock_input):
        with patch('builtins.print') as mock_print:
            with self.assertRaises(KeyboardInterrupt):
                validate_menu(self.valid_inputs)
                
    @patch('builtins.input', side_effect=[Exception("Test exception"), '3']) # check an exception.
    def test_general_exception(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, '3')
            self.assertEqual(mock_input.call_count, 2)
            error_call = any("An error occurred" in str(args[0]) for args, _ in mock_print.call_args_list)
            self.assertTrue(error_call)
            
    @patch('builtins.input', side_effect=[ValueError("Invalid value"), '3']) # check a value error.
    def test_value_error(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, '3')
            self.assertEqual(mock_input.call_count, 2)
            # Check if the error message was printed
            error_call = any("An error occurred" in str(args[0]) for args, _ in mock_print.call_args_list)
            self.assertTrue(error_call)
            
    @patch('builtins.input', side_effect=[EOFError(), '3']) # check an EOF error.
    def test_eof_error(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, '3')
            self.assertEqual(mock_input.call_count, 2)
            # Check if the error message was printed
            error_call = any("An error occurred" in str(args[0]) for args, _ in mock_print.call_args_list)
            self.assertTrue(error_call)
            
    @patch('builtins.input', side_effect=['4', '5', '6', '3']) # check repeated invalid inputs.
    def test_multiple_invalid_inputs(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, '3')
            self.assertEqual(mock_input.call_count, 4)
            self.assertEqual(mock_print.call_count, 3)

if __name__ == "__main__":
    unittest.main()