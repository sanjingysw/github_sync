name_list = ["张三", "李四", "王五", "王小二", "张三"]

#len函数可以统计列表中元素数目
number = len(name_list)
print("列表中有 %d 个元素" % number)

#count 防范可以统计列表中某个数据出现的次数
cishu = name_list.count("张三")
print("张三出现了 %d 次" % cishu)
# remove方法可以从列表中删除指定的第一个数据 括号内为数据值
name_list.remove("张三")
print(name_list)