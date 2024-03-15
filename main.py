import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a color (blue/yellow/red/green/brown/orange): ")
colors = ['blue', 'yellow', 'red', 'green', 'brown', 'orange']
all_turtles = []
y_axis = 65

for turtle_index in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    all_turtles.append(new_turtle)
    y_axis -= 26

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            race_is_on = False
            if turtle.color() == user_bet:
                print("You win!")
            else:
                print("You lose.")
            print(f"The turtle with {turtle.pencolor()} color won.")
        move = random.randint(0, 10)
        turtle.forward(move)

screen.exitonclick()
