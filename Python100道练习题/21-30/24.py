#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
lst=[1]
f1=1
f2=1
for i in range(20):
    f3=f1+f2
    f1=f2
    f2=f3
    lst.append(f3)
sum=0
for i in range(20):
    sum+=lst[i+1]/lst[i]
print(sum)