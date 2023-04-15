# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
100
50  25

'''
n = 1
height = 100
sum = 0
while n <= 10:
    if n == 1:
        sum += height
    else:
        height = height / 2
        sum += (height * 2)
    n += 1
print(sum)
