from turtle import Screen, Turtle
from random import randint, shuffle

# Set up the screen
src = Screen()
src.setup(width=600, height=500)
src.title("Turtle Race Game")

colorList = ["red", "orange", "chartreuse", "dark cyan", "dark blue", 
             "dark magenta", "light coral", "light green", "deep pink", "sandy brown"]

def create_finish_line():
    line = Turtle()
    line.hideturtle()
    line.penup()
    line.goto(280, -250)
    line.setheading(90)
    line.pensize(3)
    line.pendown()
    line.forward(500)

while True:
    src.clearscreen()
    src.bgcolor("white")
    create_finish_line()
    
    # Get number of turtles
    tn_input = src.textinput("Number of turtles?", "Enter number (max 10):")
    if tn_input is None or not tn_input.isdigit():
        print("Invalid input. Exiting.")
        break
    tn = min(int(tn_input), len(colorList))

    # Ask for bet by number
    bet_input = src.textinput("Your Bet", f"Which turtle will win? (Enter 1 to {tn}):")
    if bet_input is None or not bet_input.isdigit():
        print("Invalid bet. Exiting.")
        break
    bet = int(bet_input)
    if bet < 1 or bet > tn:
        print("Bet out of range. Exiting.")
        break

    tur_obj = []
    start_y = -((tn - 1) * 30)
    for i in range(tn):
        t = Turtle()
        t.shape("turtle")
        t.color(colorList[i])
        t.penup()
        t.goto(-280, start_y + i * 60)
        t.write(f" #{i+1}", align="left", font=("Arial", 8, "bold"))  # show turtle number
        t.showturtle()
        tur_obj.append(t)

    # Start race
    race_on = True
    while race_on:
        shuffle(tur_obj)
        for i, t in enumerate(tur_obj):
            t.forward(randint(10, 20))
            if t.xcor() >= 280:
                winner_index = i + 1
                if winner_index == bet:
                    print(f"You win! Turtle #{winner_index} ({t.pencolor()}) won.")
                else:
                    print(f"You lose! Turtle #{winner_index} ({t.pencolor()}) won.")
                race_on = False
                break

    again = src.textinput("Play again?", "Type 'yes' to race again:")
    if again is None or again.lower() != "yes":
        break

src.bye()
