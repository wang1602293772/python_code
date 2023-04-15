# 求0—7所能组成的奇数个数。
'''
奇数： 1 3 5 7

'''
n=4
sum=4
for i in range(2,9):
    if i==2:
        n*=7
        sum+=n
    else:
        n=n*8
        sum+=n
    print(sum)


