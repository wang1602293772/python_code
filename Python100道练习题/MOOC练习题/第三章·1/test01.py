# （1）创建一个空列表，命名为 names，往里面添加 Lihua、Rain、Jack、Xiuxiu、Peiqi 和 Black 元素。
names=[]
names.append('Lihua')
names.append('Rain')
names.append('Jack')
names.append('Xiuxiu')
names.append('Peiqi')
names.append('Black')
print(names)
# （2）往(1)中的 names 列表里 Black 前面插入一个 Blue。
names.insert(names.index('Black'),'Blue')
print(names)
# （3）把 names 列表中 Xiuxiu 的名字改成中文“秀秀”。
names[names.index('Xiuxiu')]='秀秀'
print(names)
# （4）创建新列表[1,2,3,4,2,5,6]，合并到 names 列表中。
new_list=[1,2,3,4,2,5,6]
names.extend(new_list)
print(names)
# （5）取出 names 列表中索引 4-7 的元素。
pop_list=[]
stay_list=[]
for i in range(4,8):
    stay_list.append(names.pop(4))
print(names)
# （6）取出 names 列表中最后 3 个元素。
new_pop_list = []
for j in range(3):
    new_pop_list.append(names.pop())
print(names)