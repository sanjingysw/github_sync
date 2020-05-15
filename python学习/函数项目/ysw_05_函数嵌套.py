def test1():
    print("1" * 50)

def test2():
    print("2" * 50)
    test1()

test1()
test2()

