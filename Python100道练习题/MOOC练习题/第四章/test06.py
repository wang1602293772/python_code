#输入93python22
w = input('请输入数字和字母构成的字符串：')
for x in w:
    if '0'<= x <= '9':
        continue
    else:
        w.replace(x,'')
print(w)
