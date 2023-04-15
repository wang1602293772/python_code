from Student import Student
from Teacher import Teacher
aa=Student('信息学院',1,'王境',21,'男')
aa.personInfo()
bb=Student('金融学院',2,'李白',21,'男')
bb.personInfo()
cc=Student('机电学院',3,'张飞',23,'女')
cc.personInfo()
teacher1=Teacher('信息学院','饥渴','王111',30,'男')
teacher1.personInfo()
aa.learn(teacher1)