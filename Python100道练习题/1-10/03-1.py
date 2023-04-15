import math
#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''
设这个数为x
'''
for i in range(-100,10000000000):
    if math.sqrt(i+100)%1==0:
        if math.sqrt(i+268)%1==0:
            print(i)
