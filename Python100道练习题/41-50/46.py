#求输入数字的平方，如果平方运算后小于 50 则退出。
flag=True
while flag:
    a=float(input('请输入计算的数字'))
    if a**2<50:
        print('计算结果为：',a**2)
        flag=False
    else:
        print('计算结果为：',a**2)