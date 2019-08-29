# 判断一个数是否素数


def is_perime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True if num != 1 else False


print(is_perime(7), is_perime(8))
