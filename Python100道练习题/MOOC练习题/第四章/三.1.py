#编程求 200 以内能被 17 整除的最大正整数。
lst=[]
for i in range(1,201):
    if i %17==0:
        lst.append(i)
print(max(lst))