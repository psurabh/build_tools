import unittest

from prime_numbers import is_prime


class TestPrimeNumbers(unittest.TestCase):
    def test_is_prime_with_prime_numbers(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(7), True)

    def test_is_prime_with_non_prime_numbers(self):
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(6), False)

if __name__ == "__main__":
    unittest.main()
