import turtle
ak = turtle.Turtle()
def fun(x,size):
        ak.speed(15)
        c = ["red","yellow","blue","green","orange","purple"]
        turtle.bgcolor("black")
        for i in range(size):
            ak.pencolor(c[i%6])
            ak.circle(3 * i)
            ak.circle(-3 * i)
            if i % 2 == 0:
                ak.left(i)
            else:
                ak.right(i)

fun(ak,176)
turtle.done()
