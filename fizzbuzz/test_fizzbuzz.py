import unittest
from fizzbuzz import multiplos


class FizzBuzzTest(unittest.TestCase):

    def test_given_3_return_fizz(self):
        actual=multiplos(3)
        expected='fizz'
        self.assertEqual(expected,actual)

    def test_two(self):
        pass


if __name__ == '__main__':
    unittest.main()
