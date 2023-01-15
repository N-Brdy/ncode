import turtle

# Créer une fenêtre pour dessiner
win = turtle.Screen()
win.bgcolor("lightblue")

# Créer un turtle pour dessiner
avion = turtle.Turtle()

# Dessiner le corps de l'avion
avion.color("red")
avion.begin_fill()
avion.forward(100)
avion.left(90)
avion.forward(50)
avion.left(90)
avion.forward(100)
avion.left(90)
avion.forward(50)
avion.end_fill()

# Dessiner les ailes
avion.color("red")
avion.begin_fill()
avion.forward(50)
avion.left(120)
avion.forward(50)
avion.left(60)
avion.forward(50)
avion.left(120)
avion.forward(50)
avion.end_fill()
avion.penup()
avion.forward(100)
avion.pendown()
avion.begin_fill()
avion.forward(50)
avion.left(120)
avion.forward(50)
avion.left(60)
avion.forward(50)
avion.left(120)
avion.forward(50)
avion.end_fill()

# Dessiner la queue
avion.color("red")
avion.begin_fill()
avion.left(120)
avion.forward(25)
avion.right(90)
avion.forward(50)
avion.right(90)
avion.forward(25)
avion.end_fill()

# Masquer le turtle
avion.hideturtle()

# Afficher la fenêtre
win.mainloop()
