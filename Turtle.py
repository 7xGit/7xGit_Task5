from turtle import Screen, Turtle
from random import randint, shuffle

src = Screen()
src.setup(width=600, height=500)
src.title("Turtle Race Game")
src.listen()

colorList = ["red", "orange", "chartreuse", "dark cyan", "dark blue", "dark magenta", "light coral", "light green", "deep pink", "sandy brown"]

# Validate number of turtles
while True:
    try:
        tn = int(src.textinput(title="Enter the number of turtles?", prompt="Enter number between 2 and 10:"))
        if 2 <= tn <= len(colorList):
            break
    except:
        pass
    src.textinput("Invalid input", "Please enter a number between 2 and 10. Press Enter to try again.")

# Prepare color options for this race
shuffle(colorList)
race_colors = colorList[:tn]

# Validate user's bet
while True:
    bet = src.textinput(title="Turtle on which you want to bet.", prompt=f"Choose from: {', '.join(race_colors)}")
    if bet in race_colors:
        break
    src.textinput("Invalid bet", f"Your bet must be one of: {', '.join(race_colors)}. Press Enter to try again.")
    

tur_obj = []
for i in range(tn):
    t = Turtle()
    t.shape("turtle")
    t.color(race_colors[i])
    t.penup()
    t.goto(-280, 200 - i * 40)  # Spread turtles vertically
    t.speed(1)
    tur_obj.append(t)

# Run the race
winner = None
while bet:
    shuffle(tur_obj)
    for i in tur_obj:
        distance = randint(15, 25)
        i.forward(distance)

        if i.xcor() > 280:
            winner = i.pencolor()
            if winner == bet:
                print(f"You win with {winner}!")
            else:
                print(f"You lose! Winning color is {winner}.")
            bet = None  # Ends the race
            break

# Show result on screen
result = Turtle()
result.hideturtle()
result.penup()
result.goto(0, -200)
result.write(f"Winner: {winner}\n{'You Win!' if winner == race_colors[race_colors.index(winner)] and winner == winner else 'You Lose!'}",
             align="center", font=("Arial", 16, "bold"))

src.exitonclick()
