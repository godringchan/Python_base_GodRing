import turtle
tpen = turtle.Pen()
#  方案1
# a = -180
# b = 180
# tpen.penup()
# tpen.goto(a, b)


# for y in range(18):
#     tpen.pendown()
#     tpen.goto((a + y*abs(a/18)), abs(b/18))
#     tpen.penup()
#     tpen.goto((a + (y+1)*abs(a/18)), b)
# tpen.goto(a, b)
# for x in range(18):
#     tpen.pendown()
#     tpen.goto((a/18), b-x*(b/18))
#     tpen.penup()
#     tpen.goto(a, b - (x+1)*(b/18))

# turtle.done()

# Todo # 方案2
def qipan(x, y, long):
    '''画棋盘'''
    tpen = turtle.Pen()
    # x = -180
    # y = 180
    # long = 360

    # start = (x, )
    tpen.penup()
    tpen.goto(x, y)
    for i in range(18):
        tpen.goto(x, y - (i+1)*(long/17))         #  18个点头尾顶点，直线中间分为17份
        tpen.pendown()
        tpen.forward(long)
        tpen.penup()
        # 横线向下，起点x不变，y变小
    y2 = y - (long/17)
    tpen.goto(x, y2)
    tpen.right(90)
    for ii in range(18):
        #  竖线向右，起点y轴不变，x增加
        tpen.goto(x + (ii)*(long/17), y2)
        tpen.pendown()
        tpen.forward(long)
        tpen.penup()
    turtle.done()


if __name__ == "__main__":
    qipan(180, -180, 60)
    print(qipan.__doc__)