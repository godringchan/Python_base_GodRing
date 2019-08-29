# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。


def max(xlist):
    m1, m2 = (xlist[0], xlist[1]) if xlist[0] > xlist[1] else (xlist[1], xlist[0])
    for index in range(2, len(xlist)):
        if m2 < xlist[index]:
            m2 = xlist[index]
        if m1 < m2:
            m1, m2 = m2, m1
    return m1, m2


if __name__ == "__main__":
    xlist = [10, 11, 15, 100, 1, 3]
    max_num, max_num2 = max(xlist)
    print(max_num, max_num2)
#   print(max(xlist))
