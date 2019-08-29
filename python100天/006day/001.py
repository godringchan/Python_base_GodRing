# 练习1：实现计算求最大公约数和最小公倍数的函数。
def gcd(x, y):
    x, y = (y, x) if x > y else (x, y)
    for i in range(x, 0, -1):
        if x % i == 0 and\
        y % i == 0:
            # print("{0}与{1}的最大公约数为{2}".format(x, y, i))
            return i
            break


def lcm(x, y):
    # print("{0}与{1}的最小公倍数数为{2}".
    #       format(x, y, ((x*y)//gcd(x, y))))
    return ((x*y)//gcd(x, y))


if __name__ == "__main__":
    print(gcd(100, 5000))
    print(lcm(1001, 1024778))