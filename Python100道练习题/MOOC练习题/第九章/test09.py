# 定义一个学生 Student 类。有下面的类属性：1）姓名 name 2）年龄 age 3）成绩 score（语文，数学，英语) [每课成绩的类型为整数]
# 类方法：1）获取学生的姓名：get_name() 2）获取学生的年龄：get_age() 3）返回 3 门科目中最高的分数。
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_max_score(self):
        return max(self.score)
zm = Student('zhangming',20,[69,88,100])
print(zm.get_name())
print(zm.get_age())
print(zm.get_max_score())