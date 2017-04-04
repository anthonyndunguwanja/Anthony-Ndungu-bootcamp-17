#Testing Prime Number Generator
'''These are tests to be passed for a program to generate prime numbers'''
import unittest
from prime_numbers import gen_primenos


class PrimeGeneratorTest(unittest.TestCase):
    def test_invalid_type_string_list(self):
        self.assertEqual(gen_primenos([]), "Integers only allowed")
    
    def test_only_positive(self):
        self.assertEqual(gen_primenos(-1), "Prime numbers cannot be less than two.")

    def test_prime_numbers(self):
        self.assertEqual(gen_primenos(10), [2, 3, 5, 7])

    def test_one(self):
        self.assertEqual(gen_primenos(1), "Zero or One cannot be prime numbers.")

    def test_invalid_type_string(self):
        self.assertEqual(gen_primenos("String"), "Only integers are allowed.")

    def test_zero(self):
        self.assertEqual(gen_primenos(0), "Zero or One cannot be prime numbers.")

if __name__ == "__main__":
    unittest.main()
    

  
