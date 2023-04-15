#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
a=12345
count=0
lst=[]
while a>0:
    lst.append(a%10)
    a=a//10
    count+=1
print(count)
lst.reverse()
print(lst)