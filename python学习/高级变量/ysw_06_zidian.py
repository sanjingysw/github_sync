xiaoming = {"name": "小明"}
# 取值的时候，如果指定 key 不存在，会报错
print(xiaoming["name"])

# 如果 key 不存在，增加键值对
xiaoming["age"] = 18
print(xiaoming)

# 如果 key 存在，修改 key 对应的值
xiaoming["name"] = "小小明"
print(xiaoming)

# pop方法删除键值对，key 不存在，会报错
xiaoming.pop("name")
print(xiaoming)

xiaoming["name"] = "小小明"
# 统计键值对数量 
print(len(xiaoming))

# 合并字典 有相同key 则覆盖
temp_dict = {"height": 1.75}
xiaoming.update(temp_dict)
print(xiaoming)

''' 
# 清空字典
xiaoming.clear()
print(xiaoming)
'''

# 遍历
for k in xiaoming:
    print("%s —— %s" % (k , xiaoming[k]))

# 实际开发中，应该将多个字典放在一个列表中进行遍历
mingdan = [{"name": "张三",
            "age": 18,
            "phone": "14455656"},
            {"name": "李四",
            "age": 19,
            "phone": "123444"}
          ]
for ren in mingdan:
    print(ren)
    print(" %s的年龄是%d岁，电话是%s。" 
           %(ren["name"], ren["age"], ren["phone"])
         )