"""
    练习：在exercise02基础上
        为插入／删除函数增加返回值与参数
"""


def verif_permissions(func):
    def wrapper(*args,**kwargs):# 合
        print("验证权限")
        return func(*args,**kwargs)# 拆
    return wrapper

@verif_permissions
def insert(data):
    print("插入数据")
    return "ok"

@verif_permissions
def delete(id):
    print("删除数据")
    return "no"

print(insert("新数据"))
print(delete(1001))
