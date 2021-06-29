from typing import ClassVar


class animal(object):
    """docstring for animal."""

    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def walk(self):
        print("I am walking")


class canine:
    def bite(self):
        print("I bite you hard!")


class dog(animal, canine):
    """docstring for dog."""

    # class data attributes
    ancestor = "BIG DOG"

    # public class method attribute
    @classmethod
    def who_i_am(cls):
        print("I am a " + cls.ancestor)

    def __init__(self, age):
        super(dog, self).__init__(age)

    def bark(self):
        print("I am: " + str(self.get_age()))

    # overloading the parent method
    def walk(self):
        print("I am walking really fast!")

    # operator overloading
    def __gt__(self, other):
        return True if self.get_age() > other.get_age() else False


puppy1 = dog(12)
puppy2 = dog(24)
print(puppy1.get_age())
puppy1.bark()
puppy1.walk()
puppy1.bite()
print(puppy1 < puppy2)
dog.who_i_am()
