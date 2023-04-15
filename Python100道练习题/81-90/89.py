#某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，
# 再将第一位和第四位交换，第二位和第三位交换。
secret=[]
for i in range(4):
    secret.append(int(input('请输入数字')))
for j in range(4):
    secret[j]+=5
for k in range(4):
    secret[k]=secret[k]%10
for m in range(2):
    secret[m],secret[len(secret)-1-m]=secret[len(secret)-1-m],secret[m]
print(secret)