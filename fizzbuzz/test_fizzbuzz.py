import unittest
from fizzbuzz import FizzBuzz

# 1. For multiples of three return “Fizz” instead of the number
# 2. For the multiples of five return “Buzz”
# 3. For numbers that are multiples of both three and five return “FizzBuzz”.


class FizzBuzzTest(unittest.TestCase):
    def test_multiple_3_should_return_fizz(self):
        self.assertEqual(FizzBuzz(3), "fizz")

    def test_multiple_5_should_return_buzz(self):
        self.assertEqual(FizzBuzz(3), "fizz")


if __name__ == '__main__':
    unittest.main()
