#利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
def print1(s:str):
    len1=len(s)-1
    if len1==0:
        print(s[0])
        return
    else:
        print(s[len1])
        len1-=1
        print1(s[:len1+1])
a='12345'
print1(a)