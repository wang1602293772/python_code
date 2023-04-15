#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
count=0
for i in (1,2,3,4):
    for j in (1,2,3,4):
        for k in (1, 2, 3, 4):
            if i!=j and i!=k and j!=k:
                print(i*100+j*10+k)
                count+=1
print(f'count={count}')
