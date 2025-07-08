num1 = 1
print(type(num1)) # <class 'bool'>

num2 = 3.1415926
print(type(num2)) # <class 'float'>

num3 = 1 + 2j
print(type(num2)) # <class 'float'>

flag1 = True
print(type(flag1)) # <class 'bool'>

flag2 = True
print(type(flag2)) # <class 'bool'>
print(isinstance(flag2, bool)) # True
print(isinstance(flag2, int)) # True
print(isinstance(bool, int)) # False
