import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from utils.validation import validate_menu

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.valid_inputs = ['1', '2', '3', 'q']
        
    def tearDown(self):
        pass

class TestValidateMenu(TestMenu):
    @patch('builtins.input', return_value='1')
    def test_valid_input_single_digit(self, mock_input):
        result = validate_menu(self.valid_inputs)
        self.assertEqual(result, '1')
        mock_input.assert_called_once()
        
    @patch('builtins.input', return_value='q')
    def test_valid_input_character(self, mock_input):
        result = validate_menu(self.valid_inputs)
        self.assertEqual(result, 'q')
        mock_input.assert_called_once()
        
    @patch('builtins.input', return_value='   2   ')
    def test_valid_input_with_whitespace(self, mock_input):
        result = validate_menu(self.valid_inputs)
        self.assertEqual(result, '2')
        mock_input.assert_called_once()
        
    @patch('builtins.input', side_effect=['4', '3'])
    def test_invalid_input_then_valid(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, '3')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\nInvalid.', end=' ')
            
    @patch('builtins.input', side_effect=['', '1'])
    def test_empty_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, '1')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\nInvalid.', end=' ')
            
    @patch('builtins.input', side_effect=['abc', '2'])
    def test_wrong_string_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, '2')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\nInvalid.', end=' ')
            
    @patch('builtins.input', side_effect=['Q', 'q'])
    def test_case_sensitive_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, 'q')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('\nInvalid.', end=' ')
            
    @patch('builtins.input', side_effect=KeyboardInterrupt)
    def test_keyboard_interrupt(self, mock_input):
        with patch('builtins.print') as mock_print:
            with self.assertRaises(KeyboardInterrupt):
                validate_menu(self.valid_inputs)
                
    @patch('builtins.input', side_effect=[Exception("Test exception"), '3'])
    def test_general_exception(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, '3')
            self.assertEqual(mock_input.call_count, 2)
            # Check if the error message was printed
            error_call = any("An error occurred" in str(args[0]) for args, _ in mock_print.call_args_list)
            self.assertTrue(error_call)
            
    @patch('builtins.input', side_effect=[ValueError("Invalid value"), '3'])
    def test_value_error(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, '3')
            self.assertEqual(mock_input.call_count, 2)
            # Check if the error message was printed
            error_call = any("An error occurred" in str(args[0]) for args, _ in mock_print.call_args_list)
            self.assertTrue(error_call)
            
    @patch('builtins.input', side_effect=[EOFError(), '3'])
    def test_eof_error(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, '3')
            self.assertEqual(mock_input.call_count, 2)
            # Check if the error message was printed
            error_call = any("An error occurred" in str(args[0]) for args, _ in mock_print.call_args_list)
            self.assertTrue(error_call)
            
    @patch('builtins.input', side_effect=['4', '5', '6', '3'])
    def test_multiple_invalid_inputs(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validate_menu(self.valid_inputs)
            self.assertEqual(result, '3')
            self.assertEqual(mock_input.call_count, 4)
            self.assertEqual(mock_print.call_count, 3)

if __name__ == "__main__":
    unittest.main()