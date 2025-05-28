from turtle import Screen, Turtle
from random import randint

def run_race():
    src = Screen()
    src.setup(width=600, height=500)
    src.title("Turtle Racing Game")

    colorList = ["red", "orange", "chartreuse", "dark cyan", "dark blue", "dark magenta", "light coral", "light green", "deep pink", "sandy brown"]

    # Input validation for number of turtles
    while True:
        tn_input = src.textinput(title="Number of Turtles", prompt=f"Enter number of turtles (2-{len(colorList)}):")
        if tn_input and tn_input.isdigit():
            tn = int(tn_input)
            if 2 <= tn <= len(colorList):
                break
        src.textinput(title="Invalid Input", prompt=f"Please enter a number between 2 and {len(colorList)}. Press OK to try again.")

    # Show available colors for betting
    available_colors = colorList[:tn]
    bet = None
    while True:
        bet = src.textinput(title="Place Your Bet", prompt=f"Choose a color to bet on:\n{', '.join(available_colors)}")
        if bet:
            bet = bet.strip().lower()
            if bet in available_colors:
                break
        src.textinput(title="Invalid Color", prompt=f"Please enter one of these colors: {', '.join(available_colors)}. Press OK to try again.")

    tur_obj = []
    start_y = -((tn - 1) * 25)
    for i in range(tn):
        t = Turtle()
        t.shape("turtle")
        t.color(available_colors[i])
        t.penup()
        t.goto(-280, start_y + i * 50)
        t.speed(1)
        tur_obj.append(t)

    race_on = True
    winner = None

    while race_on:   
        for t in tur_obj:
            t.forward(randint(15, 25))
            if t.xcor() > 280:
                winner = t.pencolor()
                race_on = False
                break

    # Announce result on the screen
    result_turtle = Turtle()
    result_turtle.hideturtle()
    result_turtle.penup()
    result_turtle.goto(0, 200)
    if winner == bet:
        result_turtle.write(f"You win! The {winner} turtle won!", align="center", font=("Arial", 18, "bold"))
    else:
        result_turtle.write(f"You lose! The {winner} turtle won!", align="center", font=("Arial", 18, "bold"))

    return src

if __name__ == "__main__":
    while True:
        src = run_race()
        again = src.textinput(title="Play Again?", prompt="Do you want to play again? (yes/no)").strip().lower()
        if again not in ("yes", "y"):
            src.bye()
            break
        src.clearscreen()
