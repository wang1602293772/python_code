##求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
a=2
n=5
s=0
while n>0:
   s+=a
   a=a*10+a%10
   n-=1
print(s)
