from package1.foo import f1
from package1.package2 import bar, cad
from .. import *  # Error, because the main module resides in the root package


f1(1, 2, 3)
bar.hello()
cad.hello(123)
