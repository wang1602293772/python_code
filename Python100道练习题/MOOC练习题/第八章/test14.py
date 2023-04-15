# 实现 isPrime 函数，参数为整数，要有异常处理。如果整数是质数，返回 True，否则返回 False
import math
def isPrime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n % i==0:
                return False
    return True
try:
    num=int(input('请输入想要判断的数'))
    if isPrime(num):
        print(num,'is Prime')
    else:
        print(num,'is not Prime')
except ValueError:
    print('请输入整数')
except:
    print('未知错误')

