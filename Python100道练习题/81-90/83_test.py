# 求0—7所能组成的奇数个数。
'''
奇数： 1 3 5 7

'''
sum=0
n=4
for i in range(1,9):
    if i==1:
        sum+=n
    elif i==2:
        n*=7
        sum+=n
    else:
        n*=8
        sum+=n
print(sum)