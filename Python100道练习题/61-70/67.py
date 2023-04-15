#输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
arr=[45,85,12,36,45]
max_num=arr[arr.index(max(arr))]
min_num=arr[arr.index(min(arr))]
max_num,arr[0]=arr[0],max_num
min_num,arr[len(arr)-1]=arr[len(arr)-1],min_num
print(arr)
