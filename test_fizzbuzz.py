from fizzbuzz import fizzbuzz
import unittest


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        for i in [3, 6, 39, 81]:
            print('Testing.....', i)
            assert fizzbuzz(i) == 'fizz'

    def test_buzz(self):
        for i in [5, 65, 85]:
            print('Testing ...', i)
            assert fizzbuzz(i) == 'buzz'

    def test_fizzbuzz(self):
        for i in [15, 45, 75]:
            print('Testing ...', i)
            assert fizzbuzz(i) == 'fizzbuzz'

    def test_number(self):
        for i in [2, 4, 88]:
            print('testing', i)
            assert fizzbuzz(i) == i
