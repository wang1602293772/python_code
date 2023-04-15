# 定 义 一 个 至 少 有 两 个 方 法 的 类 : getString: 从 控 制 台 输 入 获 取 字 符 串 printString:打印输入字符串对应的大写形式。
class String(object):
    def getString(self):
        self.str=input('请输入字符串')
    def printString(self):
        print(self.str.upper())
str1=String()
str1.getString()
str1.printString()