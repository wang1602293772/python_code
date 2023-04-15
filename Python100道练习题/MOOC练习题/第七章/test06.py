# 用户输入单价和重量，输出总价（单价*重量），要求输出结果保留 1 位小数。
price=float(input('请输入苹果的价格'))
weight=float(input('请输入苹果的重量'))
all_money=price*weight
print('%.1f'%all_money)