from Person import Person
class Teacher(Person):
    def __init__(self, college, professional, name, age, sex):
        self.college = college
        self.professional = professional
        super(Teacher, self).__init__(name, age, sex)


    def personInfo(self):
        super(Teacher, self).personInfo()
        print('学院：', self.college, '专业:', self.professional)


    @staticmethod
    def teachObj():
        print('今天讲了如何用面向对象设计程序')