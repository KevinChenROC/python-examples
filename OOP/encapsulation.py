class point:
    """docstring for point."""

    # public class data
    DEFAULT_POS = (0, 0)

    # public class method: a constructor
    def __init__(self, x, y):
        ## __x and __y are private to the object
        self.__x = x
        self.__y = y

    # public class method
    @classmethod
    def default_pos(cls):
        return cls.DEFAULT_POS

    # public instance method
    def getx(self):
        self.__getx_instance()
        return self.__x

    # private instance method
    def __getx_instance(self):
        print("private instance method: Get x...")


p = point(1, 2)
print(p.getx())
print(point.default_pos())
