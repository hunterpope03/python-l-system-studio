import sys
import os
import unittest
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from menu.settings import LSystemSettings

class TestSettings(unittest.TestCase):
    def setUp(self):
        self.obj = LSystemSettings()
        self.valid_colors = self.obj.valid_colors

    def tearDown(self):
        del self.obj

class TestValidateDrawingColor(TestSettings):
    @patch('builtins.input', return_value='')
    def test_empty_input_default(self, mock_input):
        result = self.obj.validate_drawing_color(self.valid_colors)
        self.assertEqual(result, 'red')
        mock_input.assert_called_once()
        
    @patch('builtins.input', return_value='   ')
    def test_whitespace_input_default(self, mock_input):
        result = self.obj.validate_drawing_color(self.valid_colors)
        self.assertEqual(result, 'red')
        mock_input.assert_called_once()
        
    @patch('builtins.input', return_value='red')
    def test_valid_color_red(self, mock_input):
        result = self.obj.validate_drawing_color(self.valid_colors)
        self.assertEqual(result, 'red')
        mock_input.assert_called_once()
        
    @patch('builtins.input', return_value='   blue   ')
    def test_valid_color_with_whitespace(self, mock_input):
        result = self.obj.validate_drawing_color(self.valid_colors)
        self.assertEqual(result, 'blue')
        mock_input.assert_called_once()
        
    @patch('builtins.input', side_effect=['pink', 'green'])
    def test_invalid_color(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_drawing_color(self.valid_colors)
            self.assertEqual(result, 'green')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('Invalid color. Valid colors are: ' + str(self.valid_colors) + ', please try again.')
            
    @patch('builtins.input', side_effect=['RED', 'yellow'])
    def test_case_sensitive(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_drawing_color(self.valid_colors)
            self.assertEqual(result, 'yellow')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('Invalid color. Valid colors are: ' + str(self.valid_colors) + ', please try again.')
            
    @patch('builtins.input', side_effect=['123', 'purple'])
    def test_non_string_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_drawing_color(self.valid_colors)
            self.assertEqual(result, 'purple')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('Invalid color. Valid colors are: ' + str(self.valid_colors) + ', please try again.')

class TestValidateBackgroundColor(TestSettings):
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
        
    @patch('builtins.input', return_value='black')
    def test_valid_color_black(self, mock_input):
        result = self.obj.validate_background_color(self.valid_colors)
        self.assertEqual(result, 'black')
        mock_input.assert_called_once()
        
    @patch('builtins.input', return_value='   white   ')
    def test_valid_color_with_whitespace(self, mock_input):
        result = self.obj.validate_background_color(self.valid_colors)
        self.assertEqual(result, 'white')
        mock_input.assert_called_once()
        
    @patch('builtins.input', side_effect=['magenta', 'orange'])
    def test_invalid_color(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_background_color(self.valid_colors)
            self.assertEqual(result, 'orange')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('Invalid color. Valid colors are: ' + str(self.valid_colors) + ', please try again.')
            
    @patch('builtins.input', side_effect=['BLUE', 'green'])
    def test_case_sensitive(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_background_color(self.valid_colors)
            self.assertEqual(result, 'green')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('Invalid color. Valid colors are: ' + str(self.valid_colors) + ', please try again.')
            
    @patch('builtins.input', side_effect=['%$#', 'yellow'])
    def test_non_string_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.obj.validate_background_color(self.valid_colors)
            self.assertEqual(result, 'yellow')
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_with('Invalid color. Valid colors are: ' + str(self.valid_colors) + ', please try again.')

if __name__ == "__main__":
    unittest.main()