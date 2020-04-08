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
find_name = "三"
for stu in students:
    print(stu["name"])
    if stu["name"] == find_name:
        print("找到%s了" % find_name)
        break
else:
    print("找不到%s" % find_name)
    