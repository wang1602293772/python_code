# 使用 datetime 模块，获取昨天的日期
from datetime import date, timedelta

# 获取今天的日期
today = date.today()

# 计算昨天的日期
yesterday = today - timedelta(days=1)

# 打印昨天的日期
print(yesterday)
