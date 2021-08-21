import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
# tim.color("red")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#            "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# directions = [0, 90, 180, 270]

# tim.pensize(5)
tim.speed("fastest")


def draw_spirograph(size):
    for _ in range(int(360 / size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)


draw_spirograph(5)

# for _ in range(100):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

screen = t.Screen()
screen.exitonclick()


# import heroes
# print(heroes.gen())
