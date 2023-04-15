from Area import Area
import unittest
class Test_Area(unittest.TestCase):
    def setUp(self) -> None:
        self.area=Area()
    def test_getWidth(self):
        self.assertEqual(self.area.getWidth(),100)
    def test_getLength(self):
        self.assertEqual(self.area.getWidth(),100)
    def test_getArea(self):
        self.assertEqual(self.area.getArea(),10000)
    def test_setWidth(self):
        self.area.setWidth(10)
        self.assertEqual(self.area.getWidth(),10)
    def test_setLength(self):
        self.area.setLenth(12)
        self.assertEqual(self.area.getLength(),12)
if __name__=='__main__':
    unittest.main()

