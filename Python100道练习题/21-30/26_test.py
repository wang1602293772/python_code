# 利用递归方法求5!。
def dg(n):
    if n==1:
        return 1
    else:
        return n*dg(n-1)
print(dg(5))