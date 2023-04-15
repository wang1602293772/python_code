# 用户输入一个三位以上的整数，输出其百位以上的数字。例如用
# 户输入 1234，则程序输出 12
num=int(input('请输入三位数以上的数字'))
if len(str(num))>=3:
    finally_num=num//100
print(finally_num)