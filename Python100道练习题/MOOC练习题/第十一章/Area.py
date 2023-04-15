class Area:
    def __init__(self, width=100, length=100):
        self._width = width
        self._length = length

    def getWidth(self):
        return self._width

    def getLength(self):
        return self._length

    def getArea(self):
        return self._width * self._length

    def setWidth(self, width):
        self._width = width

    def setLenth(self, length):
        self._length = length
