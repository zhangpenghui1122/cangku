"""
1.
关于操作系统的说法正确的是？(B C)
多选
A.操作系统可以与计算机硬件很好配合，
提供给其他软件操作硬件的接口
B.所有操作系统的构成都是内核，shell，文件系统和应用
C.Linux内核是开源的，遵守开源协议
D.Ubuntu，鸿蒙，安卓，Mac
os系统的内核都是Linux
"""
"""
2.
关于Linux文件系统的说法正确的是（A B D）多选
A.Linux文件系统都挂在一个根目录上
B.Linux文件系统是树形结构
C.Linux文件系统是图形结构
D.Linux文件系统中 / home
目录就是我们所说的用户主目录
"""
"""
3. )Linux
系统中
ls
命令的作用，说法不正确的是? (B )
单选
A.ls
可以查看指定目录的内容
B.ls
可以查看文件大小
C.ls
可以查看文件操作权限
D.ls
可以查看文件内容和修改时间

4.
关于绝对路径和相对路径的说法正确的是？（A B）多选
A.绝对路径是从根目录开始查找文件
B.相对路径是从当前位置查找文件
C.使用绝对路径比相对路径方便
D.使用相对路径比绝对路径方便

5.
下列哪项不是Linux操作系统的特征？（D）单选
A.Linux操作系统是开源的
B.Linux操作系统有内核，文件系统，shell，应用构成
C.Linux图形化界面和网络功能的支持较差
D.Linux操作系统是一种常用的服务器系统

6.
下列shell命令的说法正确的是（B D）?（）多选
A.mv命令可以移动文件，也可以对文件重命名
B.rm命令将文件删除到回收站
C.cp命令可以复制普通文件和目录
D.mkdir可以同时创建多个目录

7.
下列Linux文件系统的说法正确的是（A B）多选
A.Linux文件系统中 / etc多用存放配置文件
B.Linux文件系统中以.开头的是隐藏文件
C.Linux文件系统不可以分区
D.修改Linux根目录下的文件需要管理员权限

8.
在Linux系统中输入命令“ls –al
test”显示如下”-rwx - -xr - x
1
root
root
100
2019 - 12 - 20
23: 51
test”对它的含义解释错误的是（B）单选
A.这是一个文件，而不是目录
B.文件的拥有者可以对这个文件进行读、写和执行的操作
C.文件所有者可以读它，也可以执行它
D.其他所有用户只可以执行

9.
以下关于Linux超级权限的说明，不正确的是（B）单选
A.一般情况下，为了系统的安全，对于一般常规级别的应用，
不需要root用户来操作完成
B.普通用户可以通过su和sudo来获得系统的超级权限
C.修改文件权限，必须以root用户登录才能进行
D.root是系统的超级用户，
无论是否为文件和程序的所有者都具有访问权限

10.
删除文件的命令是（B）单选
A．mkdir
B.rm
C.mv
D.remove
"""
"""
编程题（每题20分，共60分）
1.
给定一个整数数组
nums
和一个目标值
target，请你在该数组中找出和为目标值的那
两个
整数，并返回他们的数组下标。假设每种输入只会对应一个答案。
但是，数组中同一个元素不能使用两遍。
（至少使用两种方法求解）
示例：给定
nums = [2, 7, 11, 15], target = 9
因为
nums[0] + nums[1] = 2 + 7 = 9
所以返回[0, 1]
"""

# target = 15
# print(list[1] + list[2])
# def twoSum1(nums: list, target: int):
#     for i in range(len(nums)):
#         # 从第二行开始
#         for j in range(i + 1, len(nums)):
#             if nums[j] == target - nums[i]:
#                 return [i, j]
# list = [2, 7,8, 11, 15]
# int=15
# print(twoSum1(nums=list, target=int))
# 方法2：
def twoSum2(nums: list, target: int):
    lookup = {}
    for i in range(len(nums)):
        tmp = target - nums[i]
        if tmp in lookup:
            return [lookup[tmp], i]
        lookup[nums[i]] = i
list = [2, 7,8, 10, 15]
int=10
print(twoSum2(nums=list, target=int))
"""
2.
给你一个
n * m
的二维数组，每个元素保证递增，每列元素保证递增，
试问如何找到某个数字，或者判断这个数字不存在。
"""
"""
3、给你一个长度为n的数组，其中只有一个数字出现了1次，
其他均出现2次，问如何快速的找到这个数字。
"""