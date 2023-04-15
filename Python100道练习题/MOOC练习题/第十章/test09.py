# 编写一个 while 循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问
# 候语，并将一条访问记录（包含姓名和访问时间两列）添加到文件 guest_book.csv 中，
# 然后询问用户是否继续输入，用户回答否，则退出 while 循环。最后将文件内容读取显
# 示到屏幕上
import time
while 1:
    name=input('请输入名字')
    content='Hello '+ name
    print(content)
    try:
        with open('e:/guest_book.csv','a')as fp1:
            fp1.write(f'{content},{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())}')
    except Exception as e:
        print('Eorro ',e)
    choice = input('否继续输入(yes/no)')
    if choice == 'no':
        break
try:
    with open('e:/guest_book.csv', 'r') as fp1:
        for line in fp1.readlines():
            print(line)
except Exception as e:
    print('Eorro',e)
