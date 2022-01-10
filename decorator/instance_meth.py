def meth_decorator(method):
   def method_wrapper(self, *args, **kwargs):
       print(self.__class__.__name__ + "::" + method.__name__ + "():")
       method(self, *args, **kwargs)
       print()

   return method_wrapper

class Foo:
   @meth_decorator
   def say_hello(self, name):
       print("Hello, %s" % name)

foo = Foo()
foo.say_hello(name="Kevin")

