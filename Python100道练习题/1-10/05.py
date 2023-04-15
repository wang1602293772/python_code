#输入三个整数x,y,z，请把这三个数由小到大输出。
#首先找到最小的数，赋值给x
x=int(input('X:'))
y=int(input('Y:'))
z=int(input('Z:'))
if x>y:
    x,y=y,x
if x > z:
    x, z = z, x
if y>z:
    y,z=z,y

print(x,y,z)
