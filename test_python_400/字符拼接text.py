import time


# a = 0
# for i in range(100):
#     a = a+ i
# print(a)

time1 = time.time()
a = ""
for i in range(1000000):
    a += "str"
time2 = time.time()

time_over1 = time2 - time1
print(time_over1)

time3 = time.time()
list_1 = list()
for i in range(1000000):
    list_1.append("str")
"".join(list_1)
time4 = time.time()
time_over2 = time4 - time3
print(time_over2)


a = "abc"
b = "d"
d = "e"
e = "".join((a,b, d))

print(e)