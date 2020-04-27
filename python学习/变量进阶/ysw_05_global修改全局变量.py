num = 10
def demo1():
    # 如果要修改全局变量，需要用global 声明一些即可
    # global 关键字会告诉解释器后面的变量是一个全局变量
    # 再使用赋值语句时，就不会创建局部变量
    # 此时全局变量num的值已经被修改为99
    global num
    num = 99
    print("demo1 is %d" % num)

def demo2():
    print("demo2 is %d" % num)

demo1()
demo2()