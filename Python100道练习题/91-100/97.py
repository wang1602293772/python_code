# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
import os
with open("./aa.txt", 'w',) as fp:
    while True:
        content =input('请输入内容')
        if content!='#':
            fp.write(content)
        else:
            break
