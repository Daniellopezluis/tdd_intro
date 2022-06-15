import unittest
import fizzbuzz


class FizzBuzzTest(unittest.TestCase):

    # add your tests here - modify however you want
    def test_multiple_of_three_returns_fizz(self):
        ret = fizzbuzz.fizzfuzz(3)
        self.assertEqual("fizz", ret)

    def test_when_not_multiple_of_three_returns_empty(self):
        ret = fizzbuzz.fizzfuzz(2)
        self.assertEqual("", ret)

if __name__ == '__main__':
    unittest.main()
