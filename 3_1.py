import unittest
from tests_sel import time, test1, test2
import sys


class TestFactorize(unittest.TestCase):
    def test_test1(self):
        self.assertEqual(test1(), "Congratulations! You have successfully registered!")
    def test_test2(self):
        self.assertEqual(test2(), "Congratulations! You have successfully registered!")
        


if __name__ == "__main__":
    unittest.main()
