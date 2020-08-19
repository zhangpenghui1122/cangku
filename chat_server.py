"""
author: Levi
email: lvze@tedu.cn
time: 2020-8-14
env: Python 3.6
socket and Process
"""

from socket import *
from multiprocessing import Process

# 服务器地址
HOST = "0.0.0.0"
PORT = 8000
ADDR = (HOST, PORT)

# 存储结构用于存储用户信息 {name:address }
user = {}


# 处理进入聊天室
def login(sock, name, addr):
    # 如果用户存在
    if name in user or "管理" in name:
        sock.sendto(b"FAIL", addr)
        return

    # 告知用户进入
    sock.sendto(b"OK", addr)
    # 告知其他用户
    msg = "欢迎 %s 进入聊天室" % name
    for i in user:
        sock.sendto(msg.encode(), user[i])
    # 增加用户
    user[name] = addr
    # print("测试:",user)


# 聊天
def chat(sock, name, content):
    msg = "%s : %s" % (name, content)
    # 循环发送
    for i in user:
        if i == name:
            continue
        sock.sendto(msg.encode(), user[i])


# 退出
def exit(sock, name):
    del user[name]  # 删除用户
    msg = "%s 退出了聊天室" % name
    # 循环发送
    for i in user:
        sock.sendto(msg.encode(), user[i])


# 子进程处理请求
def request(sock):
    # 循环接受客户端消息
    while True:
        # 所有请求都在这接受
        data, addr = sock.recvfrom(1024 * 10)
        # 对data做基本的解析
        tmp = data.decode().split(' ', 2)
        # 根据请求选择函数处理
        if tmp[0] == "L":
            # tmp --> ['L','name']
            login(sock, tmp[1], addr)
        elif tmp[0] == "C":
            # tmp -->  [C,name,content]
            chat(sock, tmp[1], tmp[2])
        elif tmp[0] == "E":
            # tmp --> [E,name]
            exit(sock, tmp[1])


# 启动函数用于搭建网络
def main():
    # UDP套接字
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)

    # 创建子进程
    p = Process(target=request, args=(sock,))
    p.daemon = True
    p.start()
    while True:
        content = input("管理员消息:")
        # 服务端退出
        if content == "exit":
            break
        msg = "C 管理员消息 "+content
        # 从父进程发送给子进程
        sock.sendto(msg.encode(),ADDR)


if __name__ == '__main__':
    main()
