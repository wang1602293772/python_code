# 对10个数进行排序。
# 冒泡排序
arr = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6]
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] > arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)


