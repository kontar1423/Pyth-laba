import unittest
from src.m3calc import Calculator  # Импортируем класс вместо функции

class TestParserCalc(unittest.TestCase):

    def setUp(self):
        # Создаем экземпляр калькулятора перед каждым тестом
        self.calc = Calculator()

    def test_sum(self):
        self.assertAlmostEqual(self.calc.calc("2 3 +"), 5.0)

    def test_subtraction(self):
        self.assertAlmostEqual(self.calc.calc("10 4 -"), 6.0)

    def test_multiplication(self):
        self.assertAlmostEqual(self.calc.calc("3 5 *"), 15.0)

    def test_division(self):
        self.assertAlmostEqual(self.calc.calc("10 2 /"), 5.0)

    def test_unare_minus(self):
        self.assertAlmostEqual(self.calc.calc("-3 4 +"), 1.0)

    def test_unare_plus(self):
        self.assertAlmostEqual(self.calc.calc("+3 2 +"), 5.0)

    def test_double_unare_minus(self):
        self.assertAlmostEqual(self.calc.calc("--2 3 +"), 5.0)

    def test_basic_brackets(self):
        self.assertAlmostEqual(self.calc.calc("( 3 4 + )"), 7.0)

    def test_double_brackets(self):
        self.assertAlmostEqual(self.calc.calc("( 2 3 + ) ( 4 5 + ) *"), 45.0)

    def test_brackets_in_brackets(self):
        self.assertAlmostEqual(self.calc.calc("5 ( 2 ( 3 4 - ) + ) *"), 5)

    def test_float_numbers(self):
        self.assertAlmostEqual(self.calc.calc("-2.5 1.5 +"), -1.0)

    def test_complex_expression(self):
        # Дополнительный тест для проверки работы нескольких операций
        self.assertAlmostEqual(self.calc.calc("2 3 + 4 *"), 20.0)

if __name__ == "__main__":
    unittest.main()