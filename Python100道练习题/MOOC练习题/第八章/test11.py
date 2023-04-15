# Python 如何定义函数，试着定义一个函数，给定 n，返回 n 以内的斐波那契数列
def fib(n):
    f1 = 1
    f2 = 1
    print(f1 , f2)
    f3=f1+f2
    while f3<n:
        print(f3)
        f3=f1+f2
        f1=f2
        f2=f3

fib(10)