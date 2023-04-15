# 猜年龄游戏。系统中设置好一个年龄（如 18），允许用户最多尝试 3 次，每次系统
# 给出提示（猜的偏大了或猜的偏小了），3 次都没猜对的话，就直接退出，如果猜对了，
# 打印恭喜信息并退出
import random
age = int(random.randint(1,101))
count=0
while count<3:
    guess_age=input('inout a number:').strip()
    if guess_age.isalpha():
        print('请输入整数数字')
        break
    else:
        guess_age=int(eval(guess_age))
    if guess_age>age:
        print('猜大了')
    elif guess_age<age:
        print('猜小了')
    else:
        print('恭喜，猜对了')
        break
    count+=1
    if count==3:
        print('机会用光了，加油')