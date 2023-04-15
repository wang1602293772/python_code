#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
str1=input('请输入想要统计的字符串')
word_count=0
space_count=0
num_count=0
other_count=0
for i in str1:
    if i.isspace():
        space_count+=1
    elif i.isdigit():
        num_count+=1
    elif i.isalpha():
        word_count+=1
    else:
        other_count+=1
print(f'字母：{word_count};数字：{num_count};空格：{space_count};其他字符：{other_count}')