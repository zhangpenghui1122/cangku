"""
    在插入和删除数据功能上,增加验证权限
    使用装饰器实现
    通过调试体会拦截的作用
"""

def verif_permissions(func):

    def wrapper(*args,**kwargs):
        print("验证权限") # 执行新功能
        return func(*args,**kwargs)  # 执行旧功能

    return wrapper
@verif_permissions
def insert(data):
    print("插入数据")
    return "ok"
@verif_permissions
def delete(id):
    print("删除数据")
    return "no"


print(insert("行数据"))
print(delete(1001))

# def new_func(func):
#     # 内部函数 -- 包新旧功能
#     def wrapper():
#         print("新功能") # 执行新功能
#         func()  # 执行旧功能
#
#     return wrapper
#
# def func01():
#     print("功能1")
#
# @new_func  # func02 = new_func(func02)
# def func02():
#     print("功能2")
#
# func01()
# func02()