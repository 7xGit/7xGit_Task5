from turtle import Screen, Turtle
from random import randint, shuffle

screen = Screen()
screen.setup(width=600, height=500)

colorList = ["red", "orange", "chartreuse", "dark cyan", "dark blue", "dark magenta", "light coral", "light green", "deep pink", "sandy brown"]
while True:
    try:
        tn = int(screen.textinput("Turtle Count", "Enter number of turtles (2–10):"))
        if 2 <= tn <= 10:
            break
    except:
        pass

available_colors = colorList[:tn]
color_prompt = "\n".join(available_colors)
while True:
    bet = screen.textinput("Your Bet", f"Choose one:\n{color_prompt}")
    if bet in available_colors:
        break

tur_obj = []
y_positions = list(range(-100, 100, int(200 / tn)))

for i in range(tn):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(available_colors[i])
    t.goto(-280, y_positions[i])
    t.speed("fastest")
    tur_obj.append(t)

announce = Turtle()
announce.hideturtle()
announce.penup()
announce.goto(0, 200)

race_on = True
while race_on:
    shuffle(tur_obj)
    for t in tur_obj:
        t.forward(randint(5, 15))
        if t.xcor() > 280:
            winner = t.pencolor()
            race_on = False
            message = f"You win! The {winner} turtle won!" if bet == winner else f"You lose! The {winner} turtle won!"
            announce.write(message, align="center", font=("Arial", 18, "bold"))
            break

screen.exitonclick()
