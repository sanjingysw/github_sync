# 应该把模块中所有全局变量定义在函数上方
# 全局变量 一般会要求加上一个前缀 比如 g_ gl_
gl_num = 10
gl_title = "大师"
gl_name = "小明"
def demo1():
    global gl_num
    gl_num = 99
    print("demo1 is %d" % gl_num)

def demo2():
    print("demo2 is %d" % gl_num)

demo1()
demo2()