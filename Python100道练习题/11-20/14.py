#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
def fj(num):
    for i in range(2,num+1):
        if num%i==0:
            num1=num%i
            if num1==1:
                return 0
            else:
                return fj(num1)
fj(90)
