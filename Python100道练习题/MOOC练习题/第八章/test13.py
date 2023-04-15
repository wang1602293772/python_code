# 用循环和递归分别实现求阶乘（n!）
#递归实现
def dg(n):
    if n==1:
        return 1
    else:
        return n * dg(n-1)
print(dg(3))
#循环实现
def xunhuan(n):
    a=1
    while a<=n:
        a*=(a+1)
    return  a
print(xunhuan(3))