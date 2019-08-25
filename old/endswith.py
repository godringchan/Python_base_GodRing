
str46 = "i love python"
print("1:",str46.endswith("n")) 
print("2:",str46.endswith("python"))
print("3:",str46.endswith("n",0,6))# 索引 i love 是否以“n”结尾。
print("4:",str46.endswith("")) #空字符
print("5:",str46[0:6].endswith("n")) # 只索引 i love
print("6:",str46[0:6].endswith("e"))
print("7:",str46[0:6].endswith(""))
print("8:",str46.endswith(("n","z")))#遍历元组的元素，存在即返回True，否者返回False
print("9:",str46.endswith(("k"," ")))

str49 = "sunck is a good good man"
print(str49.startswith("is"))

print("i"in"min")

print(["m", "i", "a", "n"].index("i"))

a = 1
assert a<2 "a超出范围"

dict1 = {"a": "A"}
c = {b: a for a, b in dict1.items()}
print(c)
print(b)

dict1 = {"a": "A"}
print(list(dict1.items())[0])
a, b = list(dict1.items())[0]
print(a)
print(b)

a , b = ("1", "2")
print(a)
print(b)


print(abs(-45))             abs取绝对值
print(abs(45))

