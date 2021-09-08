from typing import ClassVar


class animal(object):
    """docstring for animal."""

    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def walk(self):
        print("I am walking")


class Dog(animal):
    """docstring for Dog."""

    # class data attributes
    ancestor = "BIG DOG"

    # public class method attribute
    @classmethod
    def who_i_am(cls):
        print("I am a " + cls.ancestor)

    def __init__(self, age):
        super(Dog, self).__init__(age)

    def bark(self):
        # inherit get_age from animal
        print("I am: " + str(self.get_age()))

    # overloading the parent method
    def walk(self):
        print("I am walking really fast!")

    # operator overloading
    def __gt__(self, other):
        return True if self.get_age() > other.get_age() else False


puppy1 = Dog(12)
puppy2 = Dog(24)

puppy1.bark()
puppy1.walk() #override Animal.walk

# comparison operator overloading
print(puppy1 < puppy2)

#invoking class methods
Dog.who_i_am()
