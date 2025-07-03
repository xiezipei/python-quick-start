#!/usr/bin/env python3

# “测试某些东西”函数
def testSomeThing(someThing):
    print(someThing)

# # 大小于判断
# testSomeThing(1 + 1 > 0) # True

# # 打印空值
# testSomeThing(testSomeThing('')) # None

# # 空值判断 1
# testSomeThing(testSomeThing('') == None) # True

# # 空值判断 2
# a = None
# if a is None:
#     print("a is None") # a is None
# if a is not None:
#     print("a is not None")

# # 判断单例对象
# flag = True
# if flag is True:
#     print("flag is True") # flag is True
# if flag is False:
#     print("flag is False")

# # 判断两个变量是否指向同一个对象（内存对象）
# a = []
# b = a
# c = []
# testSomeThing(a is b) # True
# testSomeThing(a is c) # False

# 判断类型对象
a = []
if (type(a) is list):
    print("a is list") # a is list