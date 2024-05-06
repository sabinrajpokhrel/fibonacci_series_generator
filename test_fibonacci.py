"""this is a simple test case"""

import unittest             #built-in module
import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_with_positive_input(self):       #Case number 1
        number = 10
        result = fibonacci.get_fibonacci_series(number)
        assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

        number = 5          
        result = fibonacci.get_fibonacci_series(number)
        assert result == [0, 1, 1, 2, 3]

    def test_fibonacci_with_negative_input(self):       #Case number 2
        number = -2
        result = fibonacci.get_fibonacci_series(number)
        assert result  is False
        
    def test_fibonacci_with_zero_input(self):           #Case number 3
        number = 0
        result = fibonacci.get_fibonacci_series(number)

        assert result is False

    def test_fibonacci_with_one_input(self):
        number = 1
        result = fibonacci.get_fibonacci_series(number)
        assert result == [0]


    def test_fibonacci_with_wrong_input_type(self):
        number = 0.1
        result= fibonacci.get_fibonacci_series(number)
        assert result is  False

unittest.main()