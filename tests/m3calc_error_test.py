import unittest
from src.m3calc import calc

class TestErrorCalc(unittest.TestCase):

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

if __name__ == "__main__":
    unittest.main()
