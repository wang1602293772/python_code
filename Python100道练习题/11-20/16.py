#输出指定格式的日期。
import time
print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d',time.localtime()))
print(time.localtime(time.time()))
print(time.mktime(time.localtime()))