# 某自然数除它本身之外的所有因子之和等于该数，则该数被称为完数。请输
# 出 1000 以内的完数。
for i in range(2,1001):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i:
        print(i,'是完数')