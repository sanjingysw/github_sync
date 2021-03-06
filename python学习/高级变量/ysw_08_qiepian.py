# 切片语法：字符串[开始索引:结束索引:步长]
# 指定区间为 左闭右开 ：开始索引 >= 范围 < 结束索引
# 包括开始索引位置，不包含结束索引
# 不指定开始索引或结束索引，则默认从头开始 到末尾结束
# 步长默认为1,步长为-1代表逆向切片步长为1
# 除了步长之外，前两个冒号均不能省略

num_str = "0123456789"
# 截取从 2 ~ 5 位置 的字符串
print(num_str[2:6])
# 截取从 2 ~ 末尾 的字符串
print(num_str[2:])
# 截取从 开始 ~ 5 位置 的字符串
print(num_str[:6])
# 截取完整的字符串
print(num_str[::])
# 从开始位置，每隔一个字符截取字符串
print(num_str[::2])
# 从索引 1 开始，每隔一个取一个
print(num_str[1::2])
# 截取从 2 ~ 末尾 - 1 的字符串
print(num_str[2:-1:])
# 截取字符串末尾两个字符
print(num_str[-2::])
# 字符串的逆序（面试题），步长为-1代表逆向切片步长为1
# 如果步长为-2，代表逆向切片间隔切片
print(num_str[::-1])