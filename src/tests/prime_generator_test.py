import unittest
from components.prime_generator import PrimeGenerator

class TestPrimeGenerator(unittest.TestCase):
    def setUp(self):
        self.prime_generator = PrimeGenerator()

    def test_new_prime_generator_size_is_none(self):
        self.assertEqual(self.prime_generator.size, None)

    def test_random_number_generator(self):
        result = self.prime_generator.generate_random_number(4)
        self.assertLess(result, 16)

    def test_get_new_prime(self):
        prime_candidate = self.prime_generator.get_new_prime(4)
        if prime_candidate == 2:
            self.assertEqual(prime_candidate % 2 != 0, False)
        else:
            self.assertEqual(prime_candidate % 2 != 0, True)


    def test_check_if_even_number_is_not_prime(self):
        result = self.prime_generator.check_if_prime(830)
        self.assertEqual(result, False)
        result = self.prime_generator.check_if_prime(532)
        self.assertEqual(result, False)
        result = self.prime_generator.check_if_prime(14)
        self.assertEqual(result, False)
        result = self.prime_generator.check_if_prime(6)
        self.assertEqual(result, False)
        result = self.prime_generator.check_if_prime(88328)
        self.assertEqual(result, False)

    def test_check_if_prime_number_with_2(self):
        result = self.prime_generator.check_if_prime(2)
        self.assertEqual(result, True)

