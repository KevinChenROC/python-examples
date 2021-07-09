# This class implements our generator as an iterable object. It has to implement __iter__ and __next__ to make it iterable, keep track of the current state (the current number in this case), and take care of a StopIteration. It can be used to understand the concept behind generators. However, there is a lot of boilerplate code, and the logic is not as clear as with a simple function using the yield keyword.

import sys


class firstn:
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.n:
            cur = self.num
            self.num += 1
            return cur
        else:
            raise StopIteration()


firstn_object = firstn(1000000)
print(sum(firstn_object))
print(f"size = {sys.getsizeof(firstn_object)} bytes")
