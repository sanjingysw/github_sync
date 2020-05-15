def sum_2_num(num1, num2):
    """两个数字的求和"""
    return num1 + num2
shuzi1 = int(input("请输入数字:"))
shuzi2 = int(input("请输入数字:"))
result = sum_2_num(shuzi1, shuzi2)
print("结果是：%d + %d = %d" %(shuzi1,shuzi2,result))