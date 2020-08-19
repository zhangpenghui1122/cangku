"""
    压岁钱
        逻辑连续
            从得到1000元到花完,整个过程可以持续,不中断
"""


def give_gife_money(money):
    """
        获取压岁钱
    """
    print(f"获得了{money}元")

    def child_buy(commodity, price):
        nonlocal money
        money -= price
        print(f"购买了{commodity},花了{price},还剩下{money}元")

    return child_buy


# 利用闭包(外部栈帧不释放)实现效果
# 外部函数调用1次  -- 得钱
action = give_gife_money(1000)
# 内部函数调用多次 -- 花钱
action("变形金刚", 300)
action("奥特曼", 300)
action("芭比娃娃", 200)
action("辣条", 200)
