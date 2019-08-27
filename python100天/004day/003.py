# for 循环中利用分支求100内偶数和
sun = 0
for i in range(1, 101):
    if i % 2 == 0:  #  %取余数，//去掉余数
        sun += i
print(sun)
