#输入3个数a,b,c，按大小顺序输出。
a=float(input('input 1th number'))
b=float(input('input 2th number'))
c=float(input('input 3th number'))
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
print(a,b,c)