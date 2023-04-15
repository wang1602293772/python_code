#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
score =int(input('请输入你的分数'))
if score<0 or score >100:
    print('输入的分数有误，请重新输入')
elif score>=90:
    print('A')
elif score>=60 and score<=89:
    print('b')
else:
    print('c')