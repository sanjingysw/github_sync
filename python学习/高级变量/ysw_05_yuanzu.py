'''
yuanzu = ("张三", 18, 1.75)
print(yuanzu[2])

print(yuanzu.count(18))
print(yuanzu.index("张三"))
print(len(yuanzu))

for yuansu in yuanzu:
    print(yuansu)
print("%s 的年龄是 %d 升高是 %f" % yuanzu)
'''
num_list = [1, 2, 3, 4]
num_tuple = tuple(num_list)
num2_list = list(num_tuple)