num = 10
def demo1():
    # 希望修改全局变量的值
    # 但是 在python中 不允许直接修改全局变量的值
    # 此时 实际上是在定义一个在函数内部的局部变量
     num = 99
     print("demo1 is %d" % num)

def demo2():
    print("demo2 is %d" % num)

demo1()
demo2()