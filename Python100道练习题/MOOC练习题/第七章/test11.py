# 统计不及格的学生及成绩。要求：给定一些学生姓名和成绩，如[["张三",76],["李四
# ",45],["王五",83],["郑六",66]]，询问用户是否还要输入更多学生姓名和成绩，用户回答是
# 就继续输入（姓名和成绩用空格隔开），将用户输入保存，再次询问用户是否继续输入，
# 直到用户回答否；然后将不及格（<60）的学生名单和成绩打印。（所有输入均不考虑不
# 合法的情况）
score_list=[["张三",76],["李四",45],["王五",83],["郑六",66]]
answer='yes'
while answer=='yes':
    answer=input('是否输入数据 yes/no').lower()
    if answer=='no':
        for item in score_list:
            if item[1]<60:
                print(item)
        print('程序退出')
        break
    elif answer=='yes':
        answer1=input('输入姓名和成绩（姓名和成绩用空格隔开）')
        name,grade=answer1.split(' ')
        score_list.append([name,float(grade)])
    else:
        print('input Eorro!!!!')
        continue