"""
    装饰器
        定义:不改变旧功能,而增加新功能
        核心逻辑:拦截
                拦截对旧功能的调用,转移到了内部函数
                内部函数事先包装好了新功能与旧功能
        原理:闭包

    属性原理 day11/demo05
"""

# 需求:为功能1/2增加新功能
"""
def new_func():
    print("新功能")


def func01():
    print("功能1")


def func02():
    print("功能2")

# 旧功能 = 新功能
# func01 = new_func

# 旧功能 = 新功能 + 旧功能
func01 = new_func + func01

func01()
func02()
"""

# 外部函数 -- 得旧功能
def new_func(func):
    # 内部函数 -- 包新旧功能
    def wrapper():
        print("新功能") # 执行新功能
        func()  # 执行旧功能

    return wrapper

def func01():
    print("功能1")

@new_func  # func02 = new_func(func02)
def func02():
    print("功能2")

# # 旧功能 = 新功能 + 旧功能
# # func01 = new_func + func01
# # 内部函数 = 调用外部函数(旧功能)
# func01 = new_func(func01)
# # 调用内部函数 -- 调用wrapper函数
# func01()

func02()
