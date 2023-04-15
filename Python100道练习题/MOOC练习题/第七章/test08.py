# 死循环输入整数，输入后打印出之前输入的最大值和之前所有数字的平均数，如果输入
# 为非整数类型，则忽略；如果输入 quit 字符串或者空格，则结束循环，退出程序。
flag=''
lst=[]
while 1:
    flag=input('input:')
    if flag.isdigit() and eval(flag)%1==0:
        lst.append(eval(flag))
        print(lst)
        print('Max_num=',max(lst),'avg_num=',sum(lst)/len(lst))
    elif flag=='quit' or ' ' in flag:
        print('程序退出')
        break
    else:
        pass