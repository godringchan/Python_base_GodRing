num = input("输入一个数字:")
temp = 0 
for i in num:
    m = len(num)
    i = int(i)
    temp += i**m
    print(temp)
if temp == int(num):
    print("%s是自幂数"% num)
else:
    print("非自幂数")
    # print(temp)
    # print(num)
    # print(5**3+4**3+8**3+8**3+3**3+4**3)