a = [10, 20, 30]
b = [40, 50, 60]
print(id(a))
print(id(b))

a.append(b)
print(id(a))

print(a)
c = a + b
print(c)
print(id(c))

a.extend(b)
print(a)
print(id(a))

d = [10, 20, 30, 40, 50]
print(d[2:])
e = d[:2].extend(d[3:])
print(e)
print(id(e))
print(d)
print(id(d))

dict_1 = dict()
dict_1["man"] = "jack"
print(dict_1)


a = [["gao1", 1000, "1m71", "male"],
     ["gao2", 2000, "1m72", "female"],
     ["gao3", 3000, "1m73", "gay"]]
for m in range(3):
    for n in range(4):

        print(a[m][n], end="\t")
    print()

a = (20, 10, 30, 15)
b = sorted(a)
print(b)

a = [10, 20, 30]
b = [1, 2, 3]
c = [100, 200, 300]
print(sum(c))
d = zip(a, b, c)
print(list(d))


dict_2 = {("female", "jianyu"): "goog girl"}
print(dict_2)
d_k = list(dict_2.keys())
print(d_k[0][1])
