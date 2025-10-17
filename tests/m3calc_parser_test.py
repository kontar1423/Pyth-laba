import unittest
from src.m3calc import calc

class TestParserCalc(unittest.TestCase):

    def test_sum(self):
        self.assertAlmostEqual(calc("2 3 +"), 5.0)

    def test_subtraction(self):
        self.assertAlmostEqual(calc("10 4 -"), 6.0)

    def test_multiplication(self):
        self.assertAlmostEqual(calc("3 5 *"), 15.0)

    def test_division(self):
        self.assertAlmostEqual(calc("10 2 /"), 5.0)

    def test_unare_minus(self):
        self.assertAlmostEqual(calc("-3 4 +"), 1.0)

    def test_unare_plus(self):
        self.assertAlmostEqual(calc("+3 2 +"), 5.0)

    def test_double_unare_minus(self):
        self.assertAlmostEqual(calc("--2 3 +"), 5.0)

    def test_basic_brackets(self):
        self.assertAlmostEqual(calc("( 3 4 + )"), 7.0)

    def test_double_brackets(self):
        self.assertAlmostEqual(calc("( 2 3 + ) ( 4 5 + ) *"), 45.0)

    def test_float_numbers(self):
        self.assertAlmostEqual(calc("3.5 2.5 +"), 6.0)
        self.assertAlmostEqual(calc("-2.5 1.5 +"), -1.0)

if __name__ == "__main__":
    unittest.main()
