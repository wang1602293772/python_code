# nums = [2, 7, 11, 15, 1, 8]
nums = [2, 7, 11, 15, 1, 8]
# 请找到列表中任意相加等于 9 的元素集合，如：[(2, 7), (1,
# 8)]
for i in nums:
    for j in nums:
        if i+j==9 and i!=j:
            print(i, j)
            nums.pop(nums.index(i))
            nums.pop(nums.index(j))

