import unittest
from sel import time, reg1, reg2
import sys


class TestFactorize(unittest.TestCase):
    def test_test1(self):
        self.assertEqual(reg1(), "Congratulations! You have successfully registered!")
    def test_test2(self):
        self.assertEqual(reg2(), "Congratulations! You have successfully registered!")
        


if __name__ == "__main__":
    unittest.main()