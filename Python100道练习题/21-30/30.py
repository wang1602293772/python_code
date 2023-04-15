#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
a=123321
b=str(a)
len1=len(b)
flag=True
for i in range(len1//2):
    if b[i]!=b[len1-i-1]:
        flag=False
if flag:
    print('是回文数')
else:
    print('不是回文数')