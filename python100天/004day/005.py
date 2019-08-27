# 利用for循环制作9*9乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%s*%s=%s" % (i, j, i*j), end = "\t" )
    print()