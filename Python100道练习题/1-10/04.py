#输入某年某月某日，判断这一天是这一年的第几天？
year=int(input("请输入年份"))
month=int(input("请输入月份"))
day=int(input("请输入天数"))

all_day=365
days=0
arr1=[31,28,31,30,31,30,31,31,30,31,30,31]
if year%4==0:
    year_day=366
for i in range(1,month):
    days=days+arr1[i-1]
if year % 4 == 0 and month>2:
    days+= 1
days+=day
print(f"{year }年共有{ all_day }天，{ month }月{ day }日是本年的第{days}天")
