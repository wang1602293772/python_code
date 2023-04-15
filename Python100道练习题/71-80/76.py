# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
def even(n):
    sum=0
    for i in range(2,n+1,2):
        sum+=1/i
    return sum
def odd(n):
    sum = 0
    for i in range(1, n + 1, 2):
        sum += 1 / i
    return sum


a= int(input('请输入一个数字'))
if a<=0:
    print('输入有误，请输入正整数')
else:
    if a%2==0:
        print(even(a))
    else:
        print(odd(a))
