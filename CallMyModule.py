#Option1 to use module
import MyModule
print(MyModule.sum(12,23))
print(MyModule.mul(2,3))

#Option2 to use module
import MyModule as m
print(m.sum(12,13))
print(m.mul(7,8))

#Option3 to use module only import one function
from MyModule import sum
print(sum(12,78))

#Option4 to use module importing all function
from MyModule import *
print(mul(4,5))