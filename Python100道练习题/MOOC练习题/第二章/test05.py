#通过切片实现字符串倒序输出。
a=input('请输入一段字符串')
for i in a[::-1]:
    print(i,end=' ')