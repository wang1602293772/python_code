# 用户输入月份，并判断这个月是哪个季节。(分析：3，4，5 月----春季 6，7，8----夏
# 季 9，10，11---秋季 12，1，2----冬季)
month=int(input('请输入月份'))
if month in (3,4,5):
    print('春季')
if month in (6,7,8):
    print('夏季')
if month in (9,10,11):
    print('秋季')
if month in (12,1,2):
    print('冬季')