"""
选择题(每题10分 ,共50分)
1.	关于面向过程描述正确的是：（ C ）
A: 根据需求划分职责，然后交给不同程序员完成。
B：根据职责划分任务，然后专人实现。
C：根据解决问题步骤，然后逐步实现。
D：使用函数屏蔽过程，彰显实现细节。。

2.	关于面向对象描述正确的是：( A )
A：使用封装、继承、多态的特点解决问题
B：使用分而治之、变则疏之、高内聚、低耦合的理念解决问题
C：主要考虑算法+数据结构
D：根据需求，划分给多个程序员共同完成。

3.	class MyClass:( D )
def __init__(qtx,a,b=””):
	qtx.a = a
	qtx.b = b
	qtx.c = 100
	关于语法，下列描述正确的是：
	A：构造函数__init__的第一个参数必须是self,存储的是当前对象地址.
B: 因为参数b有默认值，所以参数a也应该有默认值。
C：构造函数不应该使用del修饰，不能使用def修饰。
D：实例变量c不能在构造函数中确定值，必须作为参数。

4.	class MyClass:（ A ）
	def __init__(qtx,a,b=""):
		qtx.a = a
		qtx.b = b
		qtx.c = 100
	  关于创建对象，下列语法正确的是：
	  A：MyClass(10,20)
	  B:  __init__(10,”20”)
	  C:  mc = MyClass(10,20,”30”)
	D:  mc = __init__(10,”20”)

5.	class MyClass:( C )
def __init__(self,a):
	self.a = a 
	mc = MyClass(10)
	关于修改实例变量，下列错误的是：
 A：mc.__dict__[“a”] = 20
 B：mc.a = 20
 C：MyClass.a = 20
 D：mc.a = “20”
编程题(50分)
根据课上讲过的薪资计算器案例，使用面向对象的方式重写薪资计算器
"""


# 根据课上讲过的薪资计算器案例，使用面向对象的方式重写薪资计算器
# 根据工资计算个人社保缴纳费用
#     步骤：在终端中录入工资,根据公式计算,显示缴纳费用
#     公式：养老保险8% + 医疗保险2% + 3元 + 失业保险0.2% + 公积金12%
class Salary:
    def __init__(self, money):
        self.money = money

    def salary01(self, x):
        print("工资为：" + str(self.money))
        x.sd(self.money)


class Salary_calculato:
    def __init__(self, endowment, medical, unemployment, fund):
        self.endowment = endowment
        self.medical = medical
        self.unemployment = unemployment
        self.fund = fund

    def sd(self, value):
        money01 = value * (self.endowment + self.medical + self.unemployment + self.fund)
        money01 += 3
        print("缴纳费用为：" + str(money01))


s01 = Salary(6000)
t01 = Salary_calculato(0.08, 0.2, 0.02, 0.12)
s01.salary01(t01)