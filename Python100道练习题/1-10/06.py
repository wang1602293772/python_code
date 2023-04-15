#斐波那契数列
f1=0
f2=1
f3=f1+f2
print(f1,f2,f3,end=',')
for i in range(1,10):
    f1=f2
    f2=f3
    f3=f1+f2
    print(f3,end=',')