import sensors_main
import unittest
from unittest.mock import patch # neede for the example integration testing.
import sys # needed for setting the command line parameters / arguments for test cases.

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
    # incorrect. To be implemented.
    def test_check_limits2(self):
        limits = [22, 18]
        result = sensors_main.check_limits(limits)
        self.assertFalse(result, False)

    # Placeholder for the test case test_check_limits3. To be designed
    # and implemented.
    def test_check_limits3(self):
        limits = [18, 18]
        result = sensors_main.check_limits(limits)
        self.assertFalse(result, False)


    @patch('builtins.print')
    def test_check_limits_integration1(self, mock_print):
        # sets command line parameters, since they are where main gets the
        # min and max temp settings
        sys.argv = [["sensors_main.py"], [22], [18]]

        # Call main with the command line parameters set up.
        sensors_main.main()

        # check that the console output is the same as the expected error message.
        mock_print.assert_called_with("Error: Incorrect command line arguments.")

        # if you want to see what's in mock_print, you can use the following
        # sys.stdout.write(str(mock_print.call_args) + "\n")
        # sys.stdout.write(str(mock_print.call_args_list) + "\n")


    # The test case test_read_sensors1 tests the read_sensors
    # to see that the length of arrays is 4 representing the 
    # readings from the four sensors.
    def test_read_sensors1(self):
        result = sensors_main.read_sensors()
        length = len(result)
        self.assertEqual(length, 4)

    # The test case test_read_sensors2 tests the read_sensors
    # to see that the first element in the 1st sensor readings is 21.2.
    def test_read_sensors2(self):
        result = sensors_main.read_sensors()
        element1 = result[0][0]
        self.assertEqual(element1, 21.2)

    # The test case test_read_sensors3 tests the read_sensors
    # to see that the third element in the 1st sensor readings is 22.2.   
    def test_read_sensors3(self):
        result = sensors_main.read_sensors()
        element2 = result[0][3]
        self.assertEqual(element2, 22.2)

    # The test case test_read_sensors4 that tests the read_sensors
    # to see that the third element in the 4th sensor reading is -13.9.
    def test_read_sensors4(self):
        result = sensors_main.read_sensors()
        element2 = result[-1][2]
        self.assertEqual(element2, -13.9)

if __name__ == '__main__':
    unittest.main()
