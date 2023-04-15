# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
'''
Monday：星期一 Tuesday：星期二 Wednesday：星期三 Thursday：星期四 Friday：星期五  Saturday：星期六 Sunday：星期日
'''
first_word=input('please input first word:')
if first_word=='M':
    print('Monday：星期一')
elif first_word=='T':
    second_word = input('please input second word :')
    if second_word=='u':
        print('Tuesday：星期二')
    elif second_word=='h':
        print('Thursday：星期四')
    else:
        print('输入有误')
elif first_word=='W':
    print('Wednesday：星期三')
elif first_word=='F':
    print('Friday：星期五')
elif first_word=='S':
    second_word = input('please input second word :')
    if second_word=='a':
        print('Saturday：星期六')
    elif second_word=='u':
        print('Sunday：星期日')
    else:
        print('输入有误')
else:
    print('输入有误')
