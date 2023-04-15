#将一个数组逆序输出。
a = [9,6,5,4,1]
#方法1
# for i in a[::-1]:
#     print(i,end=' ')

#方法2
# a.reverse()
# print(a)

#方法3
for i in range(len(a)-1,-1,-1):
    print(a[i],end=' ')