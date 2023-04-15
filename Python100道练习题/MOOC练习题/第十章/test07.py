#  在程序中预设一个 0~9 之间的整数，让用户通过键盘输入所猜的数，如果大于预设的
# 数，显示“遗憾，太大了”；小于预设的数，显示“遗憾，太小了”，如此循环，直至猜中数，
# 显示”预测 N 次，猜中了”，其中 N 是用户输入数字的次数。注意增加异常处理，即用户
# 输入为非整数类型时给出错误提示。
import random
count=0
number=random.randint(0,10)
print(number)
while 1:
    try:
        count += 1
        guess_num=input('请输入整数')
        guess_num=int(guess_num)
    except Exception as e:
        print('请输入整数',e)
    else:
        if guess_num>number:
            print('遗憾，太大了')
        elif guess_num<number:
            print('遗憾，太小了')
        else:
            print(f'预测 {count} 次，猜中了')
            break