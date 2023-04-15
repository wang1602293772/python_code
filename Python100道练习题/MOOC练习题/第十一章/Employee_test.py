from Employee import  Employee
import  unittest
class Test_Employee(unittest.TestCase):
    def setUp(self) -> None:
        self.emp=Employee('小明',15000)
    def test_default_raise_salary(self):
        self.assertEqual(self.emp.raise_salary(),15100)

    def test_raise_salary(self):
        self.assertEqual(self.emp.raise_salary(10000),25000)

if __name__=='__main__':
    unittest.main(argv=['ignored','-v'],exit=False)