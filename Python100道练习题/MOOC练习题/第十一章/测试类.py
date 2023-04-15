from Calculator import Calculator
import unittest


class Test_Calculator(unittest.TestCase):
    def test_add(self):
        cal1 = Calculator('cal1', 30)
        result = cal1.add(1, 2)
        self.assertEqual(result, 3)

    def test_minus(self):
        cal2 = Calculator('cal2', 40)
        result1 = cal2.minus(3, 1)
        self.assertEqual(result1, 2)


unittest.main(argv=['ignored', '-v'], exit=False)
