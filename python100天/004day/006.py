#  输入一个正整数，检测是否素数
import math

temp = int(input("输入一个数字"))
num = int(math.sqrt(temp))
is_prime = True
for i in range(2, num+1):
    if temp % i == 0:
        is_prime = False
        break
if is_prime and temp != 1:
    print("是一个素数")
else:
    print("不是一个素数")

    