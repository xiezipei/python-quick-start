#!/usr/bin/env python3

# 不用关键字声明变量
x = 10

# if 语句
if x > 5:
    print("大于 5")
    print("依然在 if 块内")
print("已退出 if 块")


# 函数
def greet(name):
    return "Hello " + name


# 直接调用函数
print(greet("直接调用"))


# # 被导入时才调用函数
if __name__ == "__main__":
    print(greet("导入时调用"))
