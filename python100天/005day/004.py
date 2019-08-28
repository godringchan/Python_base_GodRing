# 斐波那契数列
def fibo(num):
    x = 1
    y = 1
    for fib in range(num):
        print(x)
        x, y = y, x + y
        # print(x)


if __name__ == "__main__":
    fibo(100)