# import turtle as t
# #
# timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("blue", "yellow")
# # # #
# # #
# # #
# # # for _ in range(4):
# # #     timmy_the_turtle.forward(100)
# # #     timmy_the_turtle.left(90)
# #
# #
# # # for _ in range(20):
# # #     timmy_the_turtle.forward(5)
# # #     timmy_the_turtle.color("white")
# # #     timmy_the_turtle.forward(5)
# # #     timmy_the_turtle.color("blue")
# #
# import random
# #colours = ["medium aquamarine", "orange", "red", "green", "yellow","blue", "purple", "IndianRed", "CornflowerBlue"]
#
# # def draw_shape(num_sides):
# #      angle = 360 / num_sides
# #     for _ in range(num_sides):
# #          timmy_the_turtle.forward(100)
# #          timmy_the_turtle.right(angle)
# # #
# # # for shape_side in range(3, 11):
# # #     timmy_the_turtle.color(random.choice(colours))
# # #     draw_shape(shape_side)
# #
# #
# #
# #
# directions = [0, 90, 180, 270]
# t.colormode(255)
# #
# def random_color():
#      r = random.randint(0,255)
#      g = random.randint(0,255)
#      b = random.randint(0,255)
#      color = (r, g, b)
#      return color
# #
# timmy_the_turtle.speed("fastest")
# # for _ in range(200):
# #     timmy_the_turtle.color(random_color())
# #     timmy_the_turtle.forward(30)
# #     timmy_the_turtle.setheading(random.choice(directions))
# # #
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         timmy_the_turtle.color(random_color())
#         timmy_the_turtle.circle(100)
#         timmy_the_turtle.setheading(timmy_the_turtle.heading()+size_of_gap)
# draw_spirograph(5)
#
# screen = t.Screen()
# screen.exitonclick()

# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random
tim = t.Turtle()
tim.penup()
tim.hideturtle()
t.colormode(255)


colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.speed("fastest")

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = t.Screen()
screen.exitonclick()

