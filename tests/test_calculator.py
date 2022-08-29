# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 13:42:45 2022

@author: Karan-PC
"""
import unittest
from operations import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        '''Test case function for addition'''
        #self.calc = calculator
        result = add(4, 7)
        expected = 11
        self.assertEqual(result, expected)
        result = add(-1, 10)
        expected = 9
        self.assertEqual(result, expected)
        result = add(100, 20)
        expected = 120
        self.assertEqual(result, expected)

    def test_sub(self):
        '''Test case function for subtraction'''
        #self.calc = calculator
        result = subtract(10, 5)
        expected = 5
        self.assertEqual(result, expected)
        result = subtract(7, 8)
        expected = -1
        self.assertEqual(result, expected)
        result = subtract(123, -7)
        expected = 130
        self.assertEqual(result, expected)

    #@unittest.skip('Some reason')
    def test_mul(self):
        '''Test case function for multiplication'''
        #self.calc = calculator
        result = multiply(3, 7)
        expected = 21
        self.assertEqual(result, expected)
        result = multiply(10, -10)
        expected = -100
        self.assertEqual(result, expected)
        result = multiply(0.5, 50)
        expected = 25
        self.assertEqual(result, expected)

    def test_div(self):
        '''Test case function for division'''
        #self.calc = calculator
        result = divide(10, 2)
        expected = 5
        self.assertEqual(result, expected)
        result = divide(100, -5)
        expected = -20
        self.assertEqual(result, expected)
        result = divide(30, 3)
        expected = 10
        self.assertEqual(result, expected)
        
if __name__ == "__main__":
  unittest.main()