# #打印出杨辉三角形
arr=[]
for i in range(10):
    arr.append([])
    for j in range(i+1):
        if j==0 or j ==i:
            arr[i].append(1)
        else:
            arr[i].append(arr[i-1][j-1]+arr[i-1][j])
for i in arr:
    print(i)
