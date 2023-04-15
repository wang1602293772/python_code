#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
#设这个数为x
import  math
for i in range(168,1000000000000000000000000000):
    for j in range(1,int(math.sqrt(i))+1):
        if j*j==i:
            x=i-168
            for m in range(1, int(math.sqrt(x))+1):
                if m*m==x:
                    print(x-100)

