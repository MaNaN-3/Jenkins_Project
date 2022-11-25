#!/usr/bin/python3
import unittest

from prog1 import vowel

class TestSum(unittest.TestCase):
    def test1(self):
        """
        Test case to add two numbers
        """
        s="arr"
        result = vowel(s)
        self.assertEqual(result, 1)
    def test2(self):
        """
        Test case to add two numbers
        """
        s="aiu"
        result = vowel(s)
        self.assertEqual(result, 3)
    def test3(self):
        """
        Test case to add two numbers
        """
        s="iuq"
        result = vowel(s)
        self.assertEqual(result, 2)
    def test4(self):
        """
        Test case to add two numbers
        """
        s="Arr"
        result = vowel(s)
        self.assertNotEqual(result, 1)
    def test5(self):
        """
        Test case to add two numbers
        """
        s="AIr"
        result = vowel(s)
        self.assertNotEqual(result, 2)

if __name__ == '__main__':
    unittest.main()