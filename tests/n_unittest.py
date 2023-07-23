import unittest
from calculator_package.calculatormb import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertAlmostEqual(self.calculator.add(2), 2)
        self.assertAlmostEqual(self.calculator.add(-5), -3)
        self.assertAlmostEqual(self.calculator.add(10), 7)

    def test_subtract(self):
        self.assertAlmostEqual(self.calculator.subtract(3), -3)
        self.assertAlmostEqual(self.calculator.subtract(-5), 2)
        self.assertAlmostEqual(self.calculator.subtract(10), -8)

    def test_multiply(self):
        self.assertAlmostEqual(self.calculator.multiply(2), 0)
        self.assertAlmostEqual(self.calculator.multiply(-5), 0)
        self.calculator.add(3)
        self.assertAlmostEqual(self.calculator.multiply(4), 12)

    def test_divide(self):
        self.calculator.add(20)
        self.assertAlmostEqual(self.calculator.divide(2), 10)
        self.assertAlmostEqual(self.calculator.divide(-5), -2)
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