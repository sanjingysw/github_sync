str1 = "hello hello world!"

# 只有当字符串中需要双引号""时，才用单引号''定义字符串
str2 = '我的外号是"大西瓜"！'

'''
# 遍历字符串，字符串一个一个显示
print(str1[5])
for c in str2:
    print(c)

# 获取字符串长度，获取字符串出现的次数
print(len(str2))
print(str1.count("llo"))
#index 获取字符串第一次出现的位置 ，注意单引号双引号的配合使用
print(str2.index('"'))

# 判断字符串中是否只包含空格或者制表符
space_str = "\n\t\r  a" 
print(space_str.isspace())

# 判断字符串中是只包含数字 
# 都不能判断浮点数（小数）
# isdigit方法 还可判断 unicode数字
# isnumeric方法  除unicode数字外，还可判断汉字数字
# 实际开发中尽量使用isdecimal方法
num_str = "壹一千零一"
print(num_str)

print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())


# 判断字符串是否以某段字符开头
hello_str = "hello world"
print(hello_str.startswith("hello"))

# 判断字符串是否以某段字符结束
print(hello_str.endswith("ld"))

# 查找指定字符串，返回索引位置
# 与index区别是：如果不包含指定字符，index报错，find返回-1
print(hello_str.find("llo"))
print(hello_str.find("abc"))

# 替换字符串，会返回一个新字符串，但是不改变原字符串
print(hello_str.replace("world", "python"))
print(hello_str)


poem1 = ["登鹳雀楼",
        "作者：王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str1 in poem1:
    #print(poem_str)
    # 对齐
    print("|%s|" % poem_str1.rjust(20, "　"))


# 去除空白字符
poem2 = ["\t\n登鹳雀楼",
        "作者：王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str2 in poem2:
    # 先用strip 方法 去除字符串中的空白字符或制表符
    # 再用center 方法 居中显示
    print("|%s|" % poem_str2.strip().center(10, "　"))

        
'''

# 拆分和连接
poem_str3= "\t\n登鹳雀楼\t作者：王之涣\t白日依山尽\t\n黄河入海流\n欲穷千里目\n\n\n更上一层楼"
print(poem_str3)

# split方法 拆分字符串，返回一个列表
# split方法用分隔符(默认为空白字符即空格和制表符)把字符串拆分成一个列表。
poem_list = poem_str3.split()
print(poem_list)

# 合并，用空格作为分隔符，把列表拼接成一个字符串
result = " ".join(poem_list)
print(result)