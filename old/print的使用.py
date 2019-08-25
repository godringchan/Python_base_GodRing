print("你好")

print("你好", end="\n")     #默认\n换行

for i in range(10000):
    print(i, end="\r")      #\r回到行首

print("你好", end="")       #无内容为不换行

print("你好", end="\t")      #\t 为打印对齐符，自动对齐，不换行
# print("\n")
a = 11111
b = 22222
print(a, b )
input()


a = divmod(10,3)
print(a)