# 编程实现如下要求。
# 1）创建员工类 Employee，属性有姓名 name、能力值 ability、年龄 age（能力值为
# 100-年龄），功能有 doWork（），该方法执行一次，该员工的能力值-10。
# 2）创建老板类 Boss，属性有金钱 money,员工列表 employeeList（存储员工类对象），
# 工作量 work,功能有雇佣员工 addEmployee()，雇佣后将员工添加至列表中，雇佣一人
# money 减 5000，金额不足时不能雇佣新员工；开始工作 startWork(),工作开始后，依次
# 取出员工列表中的员工开始工作，员工能力值减少的同时总的工作量 work 也减少，当
# 工作量 work 为 0 时，工作结束，如果所有员工使用完后，依然没有完成工作，则提示
# 老板需要雇佣新员工，并打印剩余工作量
# 3）创建 Boss 类对象，默认执行雇佣 3 个员工，年龄分别为 30,40,50，然后死循环
# 开始工作，直至工作完成。
class Employee(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.ability = 100 - self.age

    def doWork(self):
        self.ability -= 10
    def __str__(self):
        return self.name


class Boss(object):
    def __init__(self,money,work):
        self.money=money
        self.work=work
        self.employeeList=[]
    def addEmployee(self,employee):
        if self.money<5000:
            print('余额不足，无法雇佣',employee.name)
        else:

            self.employeeList.append(employee)
            print(employee.name,'雇佣成功')
            self.money-=5000
    def startWork(self):
        for i in self.employeeList:
            if self.work==0:
                print('工作完成')
                break
            else:
                print(i, '开始工作')
                i.doWork()
                self.work-=10
                if self.work==0:
                    print('工作完成')
                    break
        if self.work>0:
            print('需要雇佣新员工,剩余工作量为',self.work)
wj=Boss(money=14000,work=100)
a=Employee('小李',30)
b=Employee('小张',40)
c=Employee('小徐',50)
wj.addEmployee(a)
wj.addEmployee(b)
wj.addEmployee(c)
while wj.work!=0:
    wj.startWork()

