# 查找列表元素，移除每个元素的空格，并查找以 a 或 A 开头 并且以 c 结尾的所有元素。
# li = ["alex","aric ","Alex "," Tony","rain "]
li = ["alex","aric ","Alex "," Tony","rain "]
for i in li:
    i=i.strip()
    if (i[0]=='A' or i[0]=='a' ) and i[-1]=='c':
        print(i)