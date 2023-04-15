# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr.reverse()
a = int(input('input a number:'))
for i in arr:
    if arr[0] < arr[-1] and i > a:
        arr.insert(arr.index(i), a)
        break
    if arr[0] > arr[-1] and i < a:
        arr.insert(arr.index(i), a)
        break
print(arr)
