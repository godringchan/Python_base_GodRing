
# 练习1
# f = 1.8*c + 32
f = float(input("输入华氏温度:"))
c = (f-32)/1.8
print("%.1f 华氏度等于%.1f 摄氏度" % (f, c))


# 练习2
import math
radius = float(input("请输入圆的半径："))
perimeter = 2*radius*math.pi
area = math.pi*radius*radius
print("周长为%.1f" % perimeter)
print("面积为%.1f" % area)


# 练习3
# 计算判断闰年
year = int(input("输入年份"))
is_leap = (year % 4 == 0 and
           year % 100 != 0 or
           year % 400 == 0)
print(is_leap)
