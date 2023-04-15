#模仿静态变量的用法。
class test(object):
    a=10
    def add(self):
        self.a+=1
    def pr_a(self):
        print(self.a)
t=test()
for i in range(3):
    t.add()
    t.pr_a()
