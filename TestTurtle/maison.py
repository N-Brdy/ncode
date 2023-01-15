from turtle import *

# setup(startx=800)
title("ma maison")
hideturtle()
speed(100)
# pencolor()
fillcolor("yellow")


def construire_toit(taille):
    # Toit
    penup()
    left(180)
    forward(taille)
    right(90)
    forward(taille//4)
    left(120)
    # fin du positionnement
    pendown()
    forward(taille)
    left(120)
    forward(taille)
    left(120)
    forward(taille)


def constuire_facade(taille):
    # Facade
    forward(taille)
    left(90)
    forward(taille)
    left(90)
    forward(taille)
    left(90)
    forward(taille)


def constuire_garage(taille):
    # garage
    penup()
    left(90)
    forward(taille//4)
    pendown()
    left(90)
    forward(taille//2)
    right(90)
    forward(taille//2)
    right(90)
    forward(taille//2)


def construire_maison(taille=80):
    """ Méthode de construction d'une maison """
    print(f"Construction d'une maison de taille {taille}")
    pendown()
    constuire_facade(taille)
    constuire_garage(taille)
    construire_toit(taille)
    penup()


# construire_maison(taille=80)
# setposition(-200, 0)
# construire_maison(taille=5)
# setposition(-100, 0)
# construire_maison(taille=100)
# setposition(200, 0)
# construire_maison(taille=1000)

penup()
setposition(-200, 00)
for i in range(10, 181, 10):
    sety(0)
    construire_maison(taille=i)

mainloop()
