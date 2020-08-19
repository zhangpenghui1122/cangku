"""
    装饰器 - 语法细节
        1. 将旧功能的返回值作为内函数返回值
        2. 使用*args,**kwargs作为内函数参数
           使用*args,**kwargs调用旧功能
        温馨提示:
            做好笔记,等待今后使用.
"""

def new_func(func):
    def wrapper(*args,**kwargs): # 将多个实参合为一个元组
        print("新功能")
        # 将旧功能的返回值作为内函数返回值
        result = func(*args,**kwargs)#一个元组　拆成多个　实参
        return result

    return wrapper

@new_func
def func01(p1):
    print("功能1")
    return 10

@new_func
def func02(p1, p2):
    print("功能2")
    return 20

print(func01("a"))  #
print(func02("a", p2 = "b"))  #
