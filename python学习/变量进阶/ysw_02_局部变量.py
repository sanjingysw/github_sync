def demo1():
    # 定义一个局部变量
    num = 10
    print("在demo1函数内部的变量是 %d" % num)

demo1()

def demo2():
    num = 100
    print(num)

demo1()
demo2()

print("over")

# 局部变量的生命周期，是指变量从被创建到被系统回收的过程
# 局部变量在函数执行时才会被创建
# 函数执行结束之后 局部变量  被系统回收
# 局部变量在生命周期内，可以用来存储 函数内部临时使用到的数据
# 不同函数内部 可以使用相同名字的局部变量 彼此不影响