#字符串排序
arr=[]
for i in range(3):
    arr.append(input(f'请输入第{i+1}字符串'))
arr.sort()
for i in arr:
    print(i,end=' ')