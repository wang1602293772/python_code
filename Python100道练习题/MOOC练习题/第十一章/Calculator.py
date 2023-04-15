class Calculator(object):
    name = 'Good Calculator'
    price = 20

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b
