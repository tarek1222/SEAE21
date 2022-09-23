import sensors_main
import unittest

# Unit tests implemented with Python's built-in unittest
# need to be classes, so here we use TestSensors class
# for the tests.
class TestSensors(unittest.TestCase):

    # The test case test_check_limits1 that tests the check_limits
    # with correct inputs (lower limit 18 and higher limit 22) and
    # expects the method to return True, since the limits are
    # correct.
    def test_check_limits1(self):
        limits = [18, 22]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, True)
    
    # The test case test_check_limits2 that tests the check_limits
    # with incorrect inputs (lower limit 22 and higher limit 18) and
    # expects the method to return False, since the limits are
    # incorrect.

    
    def test_check_limits2(self):
        limits = [22, 18]
        result = sensors_main.check_limits(limits)
        self.assertFalse(result, False)
        
 

    # The test case test_check_limits3 that tests the check_limits
    # with incorrect equal inputs (lower limit 18 and higher limit 18) and
    # expects the method to return False, since the limits are
    # incorrect. 

    def test_check_limits3(self):
        limits = [18, 18]
        result = sensors_main.check_limits(limits)
        self.assertFalse(result, False)

    # The test case test_check_limitsrange1 that tests the check_limitsrange
    # with correct inputs (lower limit 12 and higher limit 55)
    #  and expects the method to return True, since the limits are correct.
   
    def test_check_limitsrange1(self):
        limits = [12, 55]
        result = sensors_main.check_limitsrange(limits)
        self.assertTrue(result, True)

    # The test case test_check_limitsrange2 that tests the check_limitsrange
    # with incorrect lower limit (lower limit 1 and higher limit 55)
    # expects the method to return False, since the  lower limit is
    # incorrect.

    def test_check_limitsrange2(self):
        limits = [1, 55]
        result = sensors_main.check_limitsrange(limits)
        self.assertFalse(result, False)

    # The test case test_check_limitsrange2 that tests the check_limitsrange
    # with incorrect upper limit (lower limit 12 and higher limit 66)
    # expects the method to return False, since the  upper limit is
    # incorrect.
    
    def test_check_limitsrange3(self):
        limits = [12, 66]
        result = sensors_main.check_limitsrange(limits)
        self.assertFalse(result, False)


if __name__ == '__main__':
    unittest.main()