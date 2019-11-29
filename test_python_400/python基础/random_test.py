import random
a =  random.randint(0, 100)
print(a)

list1 = list(range(100))
b = random.choice(list1)
print(b)

c = random.sample(list1, k=3) # sample没有权重设置
print(c)


d = random.choices(list1, k=3) # choices有权重设置，权重可以理解为概率
print(d)
