# 编写程序，创建类 Temperature，其包含成员变量 degree（表示温度）以及实例方法
# ToFahrenheit（将摄氏温度转换为华氏温度）和 ToCelsius（将华氏温度转换为摄氏温度），
# 其中，（华氏度-32）*5/9=摄氏度，摄氏度*9/5+32=华氏度
class Temperature(object):
    def __init__(self,degree):
        self.degree=degree
    def ToFahrenheit(self): #将摄氏温度转换为华氏温度  华氏度-32）*5/9=摄氏度
        Fahrenheit=self.degree*9/5+32
        return Fahrenheit
    def ToCelsius(self): #将华氏温度转换为摄氏温度 摄氏度*9/5+32=华氏度
        Celsius=(self.degree-32)*5/9
        return Celsius
tem=Temperature(25)
print(tem.ToFahrenheit())
print(tem.ToCelsius())