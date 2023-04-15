# l1 = [11, 22, 33]
# l2 = [22, 33, 44]
l1 = [11, 22, 33]
l2 = [22, 33, 44]
# a、获取内容相同的元素列表
repeat_list=[]
for i in l1:
    if i in l2:
        repeat_list.append(i)
print('l1和l2两个列表相同的元素有：',repeat_list)
# b、获取 l1 中有， l2 中没有的元素列表
l1_no_repeat_list=[]
for i in l1:
    if i not in l2:
        l1_no_repeat_list.append(i)
print('l1中有，l2没有的元素有：',l1_no_repeat_list)
# c、获取 l1 和 l2 中内容都不同的元
l2_no_repeat_list=[]
for i in l2:
    if i not in l1:
        l2_no_repeat_list.append(i)
print('l2中有，l1没有的元素有：',l2_no_repeat_list)