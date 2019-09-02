"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来
不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成
一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的
人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。
由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，
哪些位置是基督徒哪些位置是非基督徒。
"""


def main():
    people = [True] * 30
    killed, num, index = 0, 0, 0
    while killed < 15:
        if people[index]:
            num += 1
            # index +=1
        if num == 9:
            people[index] = False
            num = 1
            killed += 1
        index += 1
        index %= 30   # 起到30以内循环
    for person in people:
        print("基督徒" if person else "非基督徒")
            

if __name__ == "__main__":
    main()