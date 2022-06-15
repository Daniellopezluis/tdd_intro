import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_multiple_3_should_return_fizz(self):
        self.assertEqual(FizzBuzz(3), "fizz”)


if __name__ == '__main__':
    unittest.main()
