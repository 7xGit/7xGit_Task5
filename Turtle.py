from turtle import Screen, Turtle
from random import randint

leaderboard = {}

def run_race():
    global leaderboard
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
    progress_labels = []
    start_y = -((tn - 1) * 25)
    start_x = -280
    finish_x = 280

    for i in range(tn):
        t = Turtle()
        t.shape("turtle")
        t.color(available_colors[i])
        t.penup()
        t.goto(start_x, start_y + i * 50)
        t.speed(1)
        tur_obj.append(t)

        # Progress label above each turtle
        label = Turtle()
        label.hideturtle()
        label.penup()
        label.goto(start_x, start_y + i * 50 + 20)
        label.write("0%", align="center", font=("Arial", 10, "normal"))
        progress_labels.append(label)

    race_on = True
    winner = None

    while race_on:
        for idx, t in enumerate(tur_obj):
            move = randint(15, 25)
            t.forward(move)
            # Update progress bar
            progress = int(((t.xcor() - start_x) / (finish_x - start_x)) * 100)
            progress = min(progress, 100)
            progress_labels[idx].clear()
            progress_labels[idx].goto(t.xcor(), t.ycor() + 20)
            progress_labels[idx].color(t.pencolor())  # Match label color with turtle
            progress_labels[idx].write(f"{progress}%", align="center", font=("Arial", 10, "normal"))
            if t.xcor() > finish_x:
                winner = t.pencolor()
                race_on = False
                break

    # Update leaderboard
    if winner in leaderboard:
        leaderboard[winner] += 1
    else:
        leaderboard[winner] = 1

    # Announce result on the screen
    # Animated celebration for the winner
    for t in tur_obj:
        if t.pencolor() == winner:
            # Spin and jump
            for _ in range(12):
                t.right(30)
                t.penup()
                t.forward(10)
                t.pendown()
                t.backward(10)
            # Victory lap (small circle)
            t.penup()
            t.speed(3)
            t.pendown()
            t.circle(30)
            # Firework effect (draw stars)
            t.penup()
            t.goto(t.xcor(), t.ycor() + 40)
            t.pendown()
            t.pensize(2)
            t.pencolor("gold")
            for _ in range(8):
                t.forward(30)
                t.backward(30)
                t.right(45)
            t.pensize(1)
            t.pencolor(winner)
            break

    result_turtle = Turtle()
    result_turtle.hideturtle()
    result_turtle.penup()
    result_turtle.goto(0, 200)
    if winner == bet:
        result_turtle.write(f"You win! The {winner} turtle won!", align="center", font=("Arial", 18, "bold"))
    else:
        result_turtle.write(f"You lose! The {winner} turtle won!", align="center", font=("Arial", 18, "bold"))

    # Show leaderboard
    result_turtle.goto(0, 160)
    leaderboard_str = "Leaderboard:\n" + "\n".join(
        f"{color}: {count} win(s)" for color, count in sorted(leaderboard.items(), key=lambda x: -x[1])
    )
    result_turtle.write(leaderboard_str, align="center", font=("Arial", 14, "normal"))

    return src

if __name__ == "__main__":
    while True:
        src = run_race()
        again = src.textinput(title="Play Again?", prompt="Do you want to play again? (yes/no)")
        if not again or again.strip().lower() not in ("yes", "y"):
            src.bye()
            break
        src.clearscreen()
