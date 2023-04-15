#从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
with open ('aa.txt','r')as fp1:
    content1=fp1.read()
with open ('test.txt','r')as fp2:
    content2=fp2.read()
print(content1)
print(content2)
content_all=content2+content1
with open('all.txt','w') as fp3:
    fp3.write(content_all)
