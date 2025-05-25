from turtle import Screen, Turtle
from random import randint, shuffle

src = Screen()
src.setup(width=600, height=500)
src.listen()

colorList = ["red", "orange", "chartreuse", "dark cyan", "dark blue", "dark magenta", "light coral", "light green", "deep pink", "sandy brown"]

tn = int(src.textinput(title="Enter the number of turtles?", prompt="Enter:"))
bet = src.textinput(title="Turtle on which you want to bet.", prompt="Your bet")

tur_obj = []
for i in range(tn):
    t = Turtle()
    t.shape("turtle")
    t.color(colorList[i])
    if i % 2 == 0 and i != 0:
        i = -i
        t.penup()
        t.goto(-280, i * 50)
    else:
        t.penup()
        t.goto(-280, i * 50)
        t.speed(1)
    tur_obj.append(t)

while bet:    
    shuffle(tur_obj)
    for i in tur_obj:
        distance = randint(15, 25)
        i.forward(distance)

        if i.xcor() > 280:
            if i.pencolor() == bet:
                print(f"You win with {i.pencolor()}!")
                bet = 0
            else:
                print(f"You lose! Winning color is {i.pencolor()}.")
                bet = 0
        
src.exitonclick()
