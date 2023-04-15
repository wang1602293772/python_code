#输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
a=int(input('input a number:'))
num=9
count=1
while True:
    if num % a==0:
        print(num)
        break
    else:
        num=num*10+num%10
    count+=1
print(count)