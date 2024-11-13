import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    #Additional test cases
    #Add
    def test_add1(self):
        self.assertEqual(self.calc.add(10, 20), 30)
    
    def test_add2(self):
        self.assertEqual(self.calc.add(100, 200), 300)

    #Subtract
    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(20, 10), 10)

    #Multiply
    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(10, 10), 100)

    #Divide
    def test_divide1(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        
    #Modulo
    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(20, 7), 6)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()