import unittest
import fizzbuzz


class FizzBuzzTest(unittest.TestCase):

    # add your tests here - modify however you want
    def test_multiple_of_three_returns_fizz(self):
        ret = fizzbuzz.fizzfuzz(3)
        self.assertEqual("fizz", ret)
    # add your tests here - modify however you want
    def test_multiple_of_five_returns_buzz(self):
        ret = fizzbuzz.fizzfuzz(5)
        self.assertEqual("buzz", ret)        

    # add your tests here - modify however you want
    def test_multiple_of_three_and_five_returns_fizzbuzz(self):
        ret = fizzbuzz.fizzfuzz(15)
        self.assertEqual("fizzbuzz", ret)   

    def test_when_not_multiple_of_three_nor_five_returns_tostring(self):
        ret = fizzbuzz.fizzfuzz(2)
        self.assertEqual(str(2), ret)


if __name__ == '__main__':
    unittest.main()
