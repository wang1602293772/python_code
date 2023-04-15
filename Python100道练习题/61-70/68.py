#有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
# def swap(n,m):

a=[1, 2, 3, 4, 5, 6]
m=3
a=a[m:]+a[0:3]
# for i in range(m):
#     a.insert(0,a.pop())
print(a)