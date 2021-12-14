from turtle import Turtle, Screen
import random

is_game = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet.", prompt="Which turtle do you think is going o win. Type the color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

y = -90
for _ in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[_])
    turtle_list.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y)
    y += 30

if user_bet:
    is_game = True

while is_game:
    for turtle_instance in turtle_list:
        if turtle_instance.xcor() > 230:
            if turtle_instance.pencolor() == user_bet:
                print(f"You have won! The {turtle_instance.pencolor()} turtle has crossed the finish line first.")
            else:
                print(f"You have lost. The {turtle_instance.pencolor()} turtle has crossed the finish line first.")
            is_game = False
        turtle_instance.forward(random.randint(0, 10))


screen.exitonclick()
