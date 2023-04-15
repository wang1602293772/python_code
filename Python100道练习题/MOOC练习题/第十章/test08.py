#  编写一个 while 循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问
# 候语，并将一条访问记录添加到文件 guest_book.txt 中，然后询问用户是否继续输入，
# 用户回答否，则退出 while 循环。最后将文件内容读取显示到屏幕上。（确保这个文件中
# 的每条记录都独占一行）
while 1:
    name=input('输入名字')
    content='Hello '+name
    print(content)
    try:
        with open('e:/guest_book.txt','a') as fp:
            fp.write(content+'\n')
    except Exception as e:
        print('Eorro',e)
    choice=input('否继续输入(yes/no)')
    if choice=='no':
        break
try:
    with open('e:/guest_book.txt', 'r') as fp1:
        for line in fp1.readlines():
            print(line)
except Exception as e:
    print('Eorro',e)