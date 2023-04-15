# 编写一个名为 Employee 的类，其方法__init__() 接受姓名 name 和月薪 salary，并将它
# 们都存储在属性中。编写一个 raise_salary() 方法，它默认将月薪增加 100 元，但也能够
# 接受其他 值 。 为 Employee 编 写 一 个 测 试 用 例 ， 其 中 包 含 两 个 测 试 方 法 ：
# test_default_raise_salary() 和 test _raise_salary() 。使用方法 setUp()，以免在每个测试方法中都创建新的雇员实例
class Employee(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self, salary_increase=100):
        self.salary += salary_increase
        return self.salary
