# 计算小于 100 的最大素数。
lst=[]
for i in range(2,101):
    flag=True
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
    if flag:
        lst.append(i)
print(max(lst))