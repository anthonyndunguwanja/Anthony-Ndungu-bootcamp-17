#Testing Prime Number Generator
'''These are tests to be passed for a program to generate prime numbers'''
import unittest
from prime_numbers import prime_number_generator


class PrimeGeneratorTest(unittest.TestCase):
    def test_invalid_type_string_list(self):
        self.assertEqual(prime_number_generator([]), "Integers only allowed")
    
    def test_only_positive(self):
        self.assertEqual(prime_number_generator(-1), "Prime numbers cannot be less than two.")

    def test_prime_numbers(self):
        self.assertEqual(prime_number_generator(10), [2, 3, 5, 7])

    def test_one(self):
        self.assertEqual(prime_number_generator(1), "Zero or One cannot be prime numbers.")

    def test_invalid_type_string(self):
        self.assertEqual(prime_number_generator("String"), "Only integers are allowed.")

    def test_zero(self):
        self.assertEqual(prime_number_generator(0), "Zero or One cannot be prime numbers.")

if __name__ == "__main__":
    unittest.main()
    

  
