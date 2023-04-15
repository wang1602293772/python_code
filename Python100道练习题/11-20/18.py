#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
x=int(input('请输入几个数字相加：'))
a=2
sum=0
while x>0:
    sum+=a
    a=a*10+a%10
    x-=1
print(sum)