# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
arr1 = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
arr2 = [[5,8,1],
    [6,7,3],
    [4,5,9]]
arr3=[[],[],[]]
for i in range(len(arr1)):
    for j in range(len(arr1)):
            arr3[i].append(arr1[i][j]+arr2[i][j])
print(arr3)