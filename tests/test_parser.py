import unittest
from src.parser import Parser

class TestParser(unittest.TestCase):
    def test_basic_operations(self):
        p = Parser("3+2*2")
        self.assertEqual(p.expr(), 7)

    def test_parentheses(self):
        p = Parser("1+4*0+2-3+6*8")
        self.assertEqual(p.expr(), 48)

    def test_negative_numbers(self):
        p = Parser("-2+3")
        self.assertEqual(p.expr(), 1)

    def test_float_numbers(self):
        p = Parser("3.5+2.5")
        self.assertEqual(p.expr(), 6.0)

if __name__ == "__main__":
    unittest.main()
