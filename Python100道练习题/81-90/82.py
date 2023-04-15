# 八进制转换为十进制
a=55 #十
b=0 #八进制
num=0
if a>=8:
    while a>=8:
        num= (a % 8)*(10**b)
        a=a//8
        if(a<8):
            num=num+a*(10**(b+1))
            b += 1
else:
    num=a
print(num)