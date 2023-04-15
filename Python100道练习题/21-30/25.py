# 求1+2!+3!+...+20!的和。.
sum=0
n=21
for i in range(1, n):
    a = 1
    for j in range(1,i+1):
        a *= j
    sum+=a
print(sum)
