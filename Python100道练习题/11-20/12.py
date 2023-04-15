#题目：判断101-200之间有多少个素数，并输出所有素数。
import math
count=0
for i in range(101,201):
    flag=True
    for j in range(2,int(math.sqrt(i))+1):
        if i % j ==0:
            flag=False
    if flag:
        count += 1
        print(i,end='  ')
print('总数有：',count)