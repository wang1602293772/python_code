#求100之内的素数。
import  math
for i in range(2,101):
    flag=True
    for j in range(2,i//2+1):
        if i%j==0:
            flag=False
            break
    if flag:
        print(i,'是素数')