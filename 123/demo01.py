"""
    Enclosing  外部嵌套作用域
        内部函数可以读取但是不能修改外部变量
        必须通过nonlocal声明,才可以修改.
"""

def func01():
    print("func01执行喽")
    # 相对于文件a是局部作用域变量
    # 相对于内函数是外部嵌套作用域
    a = 10

    def func02():
        print("func02执行喽")
        # 可以读取外部变量,但是不能修改
        # 通过nonlocal声明,才可以修改
        nonlocal a
        a = 20
        print(a)

    # 只能在外部函数的内部调用内函数
    func02()
    print(a)

func01()

