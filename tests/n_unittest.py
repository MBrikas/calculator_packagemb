import unittest
from calculator_package.calculatormb import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertAlmostEqual(self.calculator.add(10), 10)
        self.assertAlmostEqual(self.calculator.add(-5), 5)
        self.assertAlmostEqual(self.calculator.add(20), 25)

    def test_subtract(self):
        self.assertAlmostEqual(self.calculator.subtract(5), -5)
        self.assertAlmostEqual(self.calculator.subtract(-8), 3)
        self.assertAlmostEqual(self.calculator.subtract(10), -7)

    def test_multiply(self):
        self.assertAlmostEqual(self.calculator.multiply(2), 0)
        self.assertAlmostEqual(self.calculator.multiply(-5), 0)
        self.calculator.add(5)
        self.assertAlmostEqual(self.calculator.multiply(4), 20)

    def test_divide(self):
        self.calculator.add(40)
        self.assertAlmostEqual(self.calculator.divide(2), 20)
        self.assertAlmostEqual(self.calculator.divide(-5), -4)
        with self.assertRaises(ValueError):
            self.calculator.divide(0)

    def test_root(self):
        self.calculator.add(9)
        self.assertAlmostEqual(round(self.calculator.root(2), 0), 3)
        self.calculator.add(64)
        self.assertAlmostEqual(round(self.calculator.root(3), 0), 4.0)

    def test_reset_memory(self):
        self.calculator.add(5)
        self.calculator.reset_memory()
        self.assertEqual(self.calculator.memory, 0)


if __name__ == '__main__':
    unittest.main()