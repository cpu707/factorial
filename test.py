import unittest
from factorial import recur_factorial
# adding a commment
class TestReturnValues(unittest.TestCase):
    def test_value(self):
        """
        Test for a known return value
        """
        self.assertEqual(recur_factorial(3), 6)

if __name__  == '__main__':
    unittest.main()
