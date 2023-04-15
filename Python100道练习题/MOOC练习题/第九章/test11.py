# 1）创建 Person 类，属性有姓名、年龄、性别，创建方法 personInfo,打印这个人的信息
# 2）创建 Student 类，继承 Person 类，属性有学院 college，班级 class，重写父类 personInfo
# 方法，除调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来。创建方
# 法 learn 参数为 Teacher 对象，调用 Teacher 类的 teach 方法，接收老师教授的知识点，
# 然后打印‘老师 xxx,我终于学会了！’xxx 为老师的 teach 方法返回的信息。
# 3）创建 Teacher 类，继承 Person 类，属性有学院 college，专业 professional，重写父
# 类 personInfo 方法，除调用父类方法打印个人信息外，将老师的学院、专业信息也打印
# 出来。创建 teachObj 方法，返回信息为‘今天讲了如何用面向对象设计程序’
# 4）创建三个学生对象，分别打印其详细信息
# 5）创建一个老师对象，打印其详细信息
# 6）学生对象调用 learn 方法
class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def personInfo(self):
        print('姓名：', self.name, '年龄：', self.age, '性别：', self.sex)


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
aa=Student('信息学院',1,'王境',21,'男')
aa.personInfo()
bb=Student('金融学院',2,'李白',21,'男')
bb.personInfo()
cc=Student('机电学院',3,'张飞',23,'女')
cc.personInfo()
teacher1=Teacher('信息学院','饥渴','王111',30,'男')
teacher1.personInfo()
aa.learn(teacher1)