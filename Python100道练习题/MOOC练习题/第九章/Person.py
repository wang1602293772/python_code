class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


    def personInfo(self):
        print('姓名：', self.name, '年龄：', self.age, '性别：', self.sex)