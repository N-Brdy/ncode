from turtle import *
from time import sleep
shape("turtle")
color('red', 'yellow')
begin_fill()

position = pos()
print(position)

forward(200)
# penup()

# pendown()
left(90)
forward(50)
left(90)
forward(50)

# print(pos())
speed(1)
left(90)
forward(100)
speed(2)
right(90)
forward(200)
#speed(10)
right(135)
forward(70)
right(45)
penup()
goto(100, -25)
pendown()

forward(25)
left(90)
forward(10)
left(90)
forward(25)
left(90)
forward(10)
end_fill()
mainloop()
sleep(5)