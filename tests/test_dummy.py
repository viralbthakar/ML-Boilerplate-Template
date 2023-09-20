import unittest

# Define a simple function to be tested
def add(a, b):
    return a + b

# Create a test class that inherits from unittest.TestCase
class TestAddition(unittest.TestCase):

    # Define a test case
    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)  # Check if the result is equal to 5

    # Define another test case
    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)  # Check if the result is equal to -5

# Run the tests if this script is executed
if __name__ == '__main__':
    unittest.main()