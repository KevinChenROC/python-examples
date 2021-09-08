class Mixin1(object):
    def test(self):
        print("Mixin1")

class Mixin2(object):
    def test(self):
        print("Mixin2")

class BaseClass(object):
    """docstring for BaseClass."""

class MyClass(Mixin2, Mixin1, BaseClass):
    pass

MyClass().test()