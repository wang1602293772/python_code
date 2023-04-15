# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
a = int(input('请输入反弹的次数：'))
sum = 0
height = 100
for i in range(1, a + 1):
    if i == 1:
        sum += height
    else:
        sum += height * 2
    height = height / 2
print(f'第{a}次反弹的高度为{height}，总共经过{sum}米')
