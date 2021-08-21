from turtle import Turtle, Screen, position
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    position = -100 + turtle_index * 30
    new_turtle.goto(x=-230, y=position)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# def move_forwards():
#     tim.forward(10)


# def move_backwards():
#     tim.backward(10)


# def turn_left():
#     tim.setheading(tim.heading() + 10)


# def turn_right():
#     tim.setheading(tim.heading() - 10)


# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()


# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")

screen.exitonclick()
