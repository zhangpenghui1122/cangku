"""
练习: 模拟自动窗口售票系统 10个窗口,
同时售票,一个线程表示一个窗口 一共有500张票,
放在列表中记做T1--T500,
要求按照顺序卖出 每次买一张票会有 0.1s停顿
编程模拟这个事情
"""
from threading import Thread
from time import sleep
list=[]
for n in range(1,501):
    list.append("T"+str(n))

def sell(w):
    while list:
        print("%s 卖出：%s"%(w,list.pop(0)))
        sleep(0.1)

jobs=[]
for i in range(1,11):
    t=Thread(target=sell,args=("w%d"%i,))
    jobs.append(t)
    t.start()
[i.join()for i in jobs]

