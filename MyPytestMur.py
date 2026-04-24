def fname(x):
    a = x.split(",")
    n = []

    for i in a:
        n.append(int(i))

    n.sort()

    unq = []
    for i in n:
        if i not in unq:
            unq.append(i)

    for i in unq:
        print(i, end=" ")

    print("Кол-во чисел:", len(unq))
    return unq

def test():
    print("проведем тесты:")
    assert fname("1,2,3,3,2,1") == [1, 2, 3]
    assert fname("5,4,3,2,1") == [1, 2, 3, 4, 5]
    assert fname("10,10,10") == [10]
    assert fname("7,3,9,1,5") == [1, 3, 5, 7, 9]
    assert fname("100,50,50,25,10") == [10, 25, 50, 100]
    print("тест проведен")

fname("1,2,11,1,1,1,1,2,2,2,1,1,2,3,4,5,6,78,2,3,2,2")
# test()
