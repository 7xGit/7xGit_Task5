from turtle import Screen, Turtle
from random import randint

src = Screen()
src.setup(width=600, height=500)
src.listen()


colorList = ["red", "orange", "chartreuse", "dark cyan", "dark blue", 
             "dark magenta", "light coral", "light green", "deep pink", "sandy brown"]


tn = int(src.textinput(title="Enter the number of turtles?", prompt="Enter:"))
bet = src.textinput(title="Turtle on which you want to bet.", prompt="Your bet")


tur_obj = []
y_positions = []


start_y = 200
spacing = 400 / (tn - 1) if tn > 1 else 0

for i in range(tn):
    if tn == 1:
        y_pos = 0
    else:
        y_pos = start_y - (i * spacing)
    y_positions.append(y_pos)

for i in range(tn):
    t = Turtle()
    t.shape("turtle")
    t.color(colorList[i % len(colorList)]) 
    t.penup()
    t.goto(-280, y_positions[i])
    t.speed(1)
    tur_obj.append(t)

# Race loop
race_finished = False
while not race_finished:
    for turtle in tur_obj:
        distance = randint(1, 10)  
        turtle.forward(distance)
        
        if turtle.xcor() >= 280:
            winner_color = turtle.pencolor()
            if winner_color == bet:
                print(f"You win! {winner_color.title()} turtle won!")
            else:
                print(f"You lose! {winner_color.title()} turtle won, but you bet on {bet}.")
            race_finished = True
            break

src.exitonclick()