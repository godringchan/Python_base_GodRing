# 打印星星三角形
row = int(input("输入行数"))
for i in range(row+1):
    for x in range(i):
        print("*", end="")
    print()


for i in range(row):
    for j in range(row):
        if j < row - i -1:
            print(" ", end="")
        else:
            print("*", end="")
    print()


for i in range(row):
    for _ in range(row - i -1):
        print(" ", end="")
    for _ in range((i*2 )+ 1):
        print("*", end="")
    print()
