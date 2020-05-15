name_list = ["zhangsan", "lisi", "wangwu"]
# 输出
print(name_list)

# 取值：根据索引位置，取值
print(name_list[2])

# 取索引:根据内容，确定位置
print(name_list.index("lisi"))

# 修改
name_list[1] = "李四"
print(name_list)

# 增加
# append方法可在列表末尾增加数据
name_list.append("王小二")
print(name_list)
# insert方法可在列表指定索引位置插入数据
name_list.insert(1,"小美眉")
print(name_list)
# extend方法可把另一个列表完整内容追加到当前列表末尾
temp_list = ["孙悟空", "猪八戒", "沙悟净"]
name_list.extend(temp_list)
print(name_list)

# 删除
# remove方法可以从列表中删除指定的第一个数据 括号内为数据值
name_list.remove("wangwu")
print(name_list)
# pop方法默认情况下删除列表中最后一个数据
name_list.pop()
print(name_list)
#pop方法可以从列表中删除指定索引的数据 括号内为索引
name_list.pop(3)
print(name_list)
#del方法可以从列表中删除指定索引的数据 del本质上是把一个变量从内存删除
del name_list[1]
print(name_list)
#clear方法可以清空列表所有数据
name_list.clear()
print(name_list)


