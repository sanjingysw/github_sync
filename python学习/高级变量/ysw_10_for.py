for num in [1, 2, 3]:
    print(num)

    if num == 0:
        print("条件满足，循环中断")
        break
else:
    print("完整遍历之后，条件还是不满足")
print("结束")