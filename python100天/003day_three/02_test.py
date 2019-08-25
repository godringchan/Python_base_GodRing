x = float(input("请输入x的值"))
if x > 1:
    y = 3*x - 5
elif x < -1:
    y = 5*x + 3
else:
    y = x + 2
print("f(%.1f)等于%.1f" % (x, y))