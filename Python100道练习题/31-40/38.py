#求一个3*3矩阵主对角线元素之和。
arr=[[1, 2, 3], [4, 5, 6], [1, 8, 9]]
sum=0
# for i in range(3):
#     arr.append([])
#     for j in range(3):
#         arr[i].append(int(input(f'请输入第{i+1}行第{j+1}个数字')))
for i in range(3):
    for j in range(3):
        if j == len(arr)-i+1:
            sum+=arr[i][j]
print(sum)

