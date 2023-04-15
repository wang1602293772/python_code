from Person import Person
class Student(Person):
    def __init__(self, college, class_, name, age, sex):
        self.college = college
        self.class_ = class_
        super(Student, self).__init__(name, age, sex)


    def personInfo(self):
        super(Student, self).personInfo()
        print('学院：', self.college, '班级:', self.class_)


    def learn(self, teacher):
        teacher.teachObj()
        print('老师', teacher.name, ',我终于学会了！')