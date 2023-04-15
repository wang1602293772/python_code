k = 0
while True:
    s=input('请输入 q 退出:')
    if s == 'q':
        k += 1
        continue
    else:
        k += 2
        break
print(k)