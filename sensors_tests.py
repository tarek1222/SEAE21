import sensors_main
import unittest
from unittest.mock import patch 
import sys 


class TestSensors(unittest.TestCase):
    
    def test_check_limits1(self):
        limits = [-12, 55]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, True)
    
    
    def test_check_limits2(self):
        limits = [55, -12]
        result = sensors_main.check_limits(limits)
        self.assertFalse(result, False)

   
    def test_check_limits3(self):
        limits = [-12, -12]
        result = sensors_main.check_limits(limits)
        self.assertFalse(result, False)

   
    @patch('builtins.print')
    def test_check_limits_integration1(self, mock_print):
       
        sys.argv = [["sensors_main.py"], [55], [-12]]

        sensors_main.main()

        
        mock_print.assert_called_with("Error: Incorrect command line arguments.")


if __name__ == '__main__':
    unittest.main()