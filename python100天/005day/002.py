# 寻找完美数
import math
list1 = list()
for i in range(1, 100):
    temp = 1
    end = int(math.sqrt(i))
    for j in range(2, end + 1):
        if i % j == 0:
            temp += j
            temp += int(i/j)
    # print(temp)
    if temp == i:
        list1.append(i)
print(list1)
# print(int(math.sqrt(6)))