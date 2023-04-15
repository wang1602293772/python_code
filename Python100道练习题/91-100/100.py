#列表转换为字典
i = ['a', 'b']
l = [1, 2]
aa=dict(zip(i,l))
print(aa)
dic={i:l for i,l in zip(i,l)}
print(dic)
# dic=dict{i}
# print(dic)