# 判断是否回文数
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


# 判断一个数是否素数


def is_perime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True if num != 1 else False


if __name__ == "__main__":
    num = int(input("请输入数字"))
    if is_palindrome(num) and is_perime(num):
        print("%d是回文数且是素数" % num)
    else:
        print("并非回文素数")
