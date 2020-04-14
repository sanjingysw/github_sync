students = [
    {"name": "张三",
     "age": 18,
     "gender": True,
     "height": 1.75,
     "weight": 70.5},
     {"name": "李四",
     "age": 22,
     "gender": False,
     "height": 1.65,
     "weight": 55.5},   
            ]
find_name = "1"
for stu in students:
    print(stu["name"])
    if stu["name"] == find_name:
        print("找到%s了" % find_name)
        # 如果已经找到 直接break跳出循环
        break
else:
    # 如果希望搜索列表，所有字典循环完成，没有发现目标
    # 还希望得到一个提示，可输出一段文字
    print("找不到%s" % find_name)
    