#时间函数举例4,一个猜数游戏，判断一个人反应快慢。
import random
import time

random_num=int(random.randint(1,500))
start_time=time.time()
while True:
    a= int(input('请输入猜想的数字'))
    if a > random_num:
        print('猜大了')
    elif a < random_num:
        print('猜小了')
    else:
        print('猜中了')
        break
end_time=time.time()
gap_time=end_time-start_time
print('用时%.0fs'%gap_time)