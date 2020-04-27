# 应该把模块中所有全局变量定义在函数上方
num = 10
title = "大师"
name = "小明"
def demo1():
    global num
    num = 99
    print("demo1 is %d" % num)

def demo2():
    print("demo2 is %d" % num)

demo1()
demo2()