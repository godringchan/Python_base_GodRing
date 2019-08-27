# 求两个数的最大公约数和最小公倍数
x = int(input("x = "))
y = int(input("y = "))
if x > y:
    x, y = y, x     # 通过xy互换，确保x是最小的数
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print("%d 和 %d 的最大公约数为%d" % (x, y, factor))
        print("%d 和 %d 的最小公倍数 %d" % (x, y, (x*y)//factor))
        break
