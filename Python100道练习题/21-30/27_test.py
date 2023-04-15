#利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
s=input('input a str')
def reverse(s:str):
    n=len(s)-1
    if n==0:
        print(s[0],end='')
        return
    else:
        print(s[n],end='')
        n=n-1
        reverse(s[0:n+1])
reverse(s)