#Square.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors =["red","yellow","blue","green"]
for i in range(1000):
    t.pencolor(colors[i%4])
    t.forward(i)
    t.left(91)  # 角度
