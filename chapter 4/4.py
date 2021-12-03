import math
import turtle;


def drawSquare(t, distance):
    for i in range(4):
        t.fd(distance)
        t.lt(90)


def drawPolygon(t, distance, n):
    for i in range(n):
        t.fd(distance)
        t.lt(360/n)


def drawCircle(t, radius):
    umfang = math.pi * 2 * radius
    drawPolygon(t, umfang/360, 360);


def drawArc(t, radius, angle):
    umfang = math.pi * 2 * radius + (angle/360)
    drawPolygon(t, umfang / 360, 360, angle);


def drawPolygon(t, distance, n, angle):
    for i in range(n):
        t.fd(distance)
        t.lt(angle/n)


if __name__ == '__main__':
    bob = turtle.Turtle()
    print(bob)
    drawArc(bob, 50, 270);
    turtle.mainloop()
