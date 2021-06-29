class point:
    """docstring for point."""

    def __init__(self, x, y):
        ## __x and __y are private to the object
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x


p = point(1, 2)
print(p.getx())
