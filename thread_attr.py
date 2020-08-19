"""
线程属性演示
"""
from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target = fun)

# 分支线程随主线程退出
t.setDaemon(True)

t.start()

t.setName("tarena")
print(t.getName())
print("is Alive:",t.is_alive())