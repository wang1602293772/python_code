# 海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
# 第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，
# 问海滩上原来最少有多少个桃子？
for i in range(200, 5000):
    a = 0
    flag = None
    num = i
    while a < 5 and i > 0:
        if (num - 1) % 5 == 0:
            flag = True
            a += 1
        else:
            flag = False
            break
        num -= ((num - 1) / 5 + 1)
    if flag:
        print(i)
