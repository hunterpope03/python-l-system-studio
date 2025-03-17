import sys
import os
import unittest
from unittest.mock import patch # import proper absolute import and testing libraries.

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from menu.settings import LSystemSettings # import class to test.

class TestSettings(unittest.TestCase):
    def setUp(self): # create an instance of LSystemSettings before every test.
        self.obj = LSystemSettings()
        self.valid_colors = self.obj.valid_colors

    def tearDown(self): # delete the instance of LSystemParser after each test.
        del self.obj

class TestValidateDrawingColor(TestSettings): # tests for the validate_drawing_color method.
    @patch('builtins.input', return_value='')
    def test_valid_empty(self, mock_input): # check blank input keeping default value.
        result = self.obj.validate_drawing_color(self.valid_colors)
        self.assertEqual(result, 'red')
        mock_input.assert_called_once()
        
    @patch('builtins.input', return_value='   ')
    def test_valid_whitespace(self, mock_input): # check whitespace input keeping default value.
        result = self.obj.validate_drawing_color(self.valid_colors)
        self.assertEqual(result, 'red')
        mock_input.assert_called_once()
        
    @patch('builtins.input', return_value='     blue ')
    def test_valid_color(self, mock_input): # check a valid color with whitespace.
        result = self.obj.validate_drawing_color(self.valid_colors)
        self.assertEqual(result, 'blue')
        mock_input.assert_called_once()
        
    @patch('builtins.input', side_effect=['pink', 'green'])
    def test_invalid_color(self, mock_input): # check an invalid color raising an error.
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_drawing_color(self.valid_colors)
            self.assertEqual(result, 'green')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('Invalid color. Valid colors are: ' + str(self.valid_colors) + ', please try again.')
            
    @patch('builtins.input', side_effect=['RED', 'yellow'])
    def test_invalid_case(self, mock_input): # check an valid color but in the wrong case raising an error.
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_drawing_color(self.valid_colors)
            self.assertEqual(result, 'yellow')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('Invalid color. Valid colors are: ' + str(self.valid_colors) + ', please try again.')
            
    @patch('builtins.input', side_effect=['123', 'purple'])
    def test_invalid_number(self, mock_input): # check a numeric input raising an error.
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_drawing_color(self.valid_colors)
            self.assertEqual(result, 'purple')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('Invalid color. Valid colors are: ' + str(self.valid_colors) + ', please try again.')

class TestValidateBackgroundColor(TestSettings): # same tests for the validate_background_color method.
    @patch('builtins.input', return_value='')
    def test_empty_input_default(self, mock_input):
        result = self.obj.validate_background_color(self.valid_colors)
        self.assertEqual(result, 'black')
        mock_input.assert_called_once()
        
    @patch('builtins.input', return_value='   ')
    def test_whitespace_input_default(self, mock_input):
        result = self.obj.validate_background_color(self.valid_colors)
        self.assertEqual(result, 'black')
        mock_input.assert_called_once()
        
    @patch('builtins.input', return_value='     orange')
    def test_valid_color_black(self, mock_input):
        result = self.obj.validate_background_color(self.valid_colors)
        self.assertEqual(result, 'black')
        mock_input.assert_called_once()
        
    @patch('builtins.input', side_effect=['magenta', 'orange    '])
    def test_invalid_color(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_background_color(self.valid_colors)
            self.assertEqual(result, 'orange')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('Invalid color. Valid colors are: ' + str(self.valid_colors) + ', please try again.')
            
    @patch('builtins.input', side_effect=['BLUE', '     green'])
    def test_case_sensitive(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_background_color(self.valid_colors)
            self.assertEqual(result, 'green')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('Invalid color. Valid colors are: ' + str(self.valid_colors) + ', please try again.')
            
    @patch('builtins.input', side_effect=['%$#', 'yellow '])
    def test_non_string_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_background_color(self.valid_colors)
            self.assertEqual(result, 'yellow')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('Invalid color. Valid colors are: ' + str(self.valid_colors) + ', please try again.')

if __name__ == "__main__":
    unittest.main()