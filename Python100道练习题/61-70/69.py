#有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
arr=[]
for i in range(1,11):
    arr.append(i)
arr2=arr.copy()
flag=0
while len(arr2)!=1:
    del_arr=[]
    for i in range(len(arr2)):
        flag += 1
        if flag%3==0:
            del_arr.append(arr2[i])
    for i in del_arr:
        arr2.remove(i)
print(arr2)