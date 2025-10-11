import unittest
from src.m3calc import calc

class TestCalc(unittest.TestCase):

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

    def test_empty_brackets(self):
        with self.assertRaises(ValueError) as cm:
            calc("( ( ) 3 4 + )")
        self.assertEqual(str(cm.exception), "Empty brackets")

    def test_wrong_brackets(self):
        with self.assertRaises(ValueError) as cm:
            calc("( 2 3 +")
        self.assertEqual(str(cm.exception), "Wrong input with ()")

    def test_unknown_operand(self):
        with self.assertRaises(ValueError) as cm:
            calc("2 3 ^")
        self.assertEqual(str(cm.exception), "Unknown operand: ^")

    def test_not_enough_numbers(self):
        with self.assertRaises(ValueError) as cm:
            calc("2 +")
        self.assertEqual(str(cm.exception), "Not enough numbers for operation")

    def test_left_elements(self):
        with self.assertRaises(ValueError) as cm:
            calc("2 3 4 +")
        self.assertEqual(str(cm.exception), "More than 1 numbers in stack left")

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as cm:
            calc("5 0 /")
        self.assertEqual(str(cm.exception), "Cannot divide by zero")

    def test_float_numbers(self):
        self.assertAlmostEqual(calc("3.5 2.5 +"), 6.0)
        self.assertAlmostEqual(calc("-2.5 1.5 +"), -1.0)

if __name__ == "__main__":
    unittest.main()
