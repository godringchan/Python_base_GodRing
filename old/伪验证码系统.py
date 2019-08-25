import random


question_a = random.randint(1, 10)
question_b = random.randint(1, 10)
answer = question_a + question_b
print("请输入验证码%s+ %s= ____" % (question_a, question_b,), end="")
try:
    a = int(input(""))
    if a == question_a + question_b:
        print("pass")
    else:
        print("验证码错误")
except Exception:
    print("输入错误")

# for i in range(1,1000000):
#     print(i, end="\r")