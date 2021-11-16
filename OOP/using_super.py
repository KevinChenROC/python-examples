class A:
    def __init__(self, name):
        self.name = name

    def message(self, source):
        print(f"From: {source}, class: A, object: {self.name}")


class B(A):
    def __init__(self, name):
        self.name = name

    def message(self, source):
        print(f"From: {source}, class: B, object: {self.name}")


class C(B):
    def __init__(self, name):
        self.name = name

    def message(self, source):
        print(f"From: {source}, class: C, object: {self.name}")


a = A("a")
b = B("b")
c = C("c")
