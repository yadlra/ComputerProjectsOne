import turtle
import random

def draw_circle(t, radius):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)

def draw_inner_pattern(t, angle, distance):
    t.penup()
    t.home()
    t.setheading(angle)
    t.forward(distance)
    t.pendown()

def draw_dot(x, y):
    t.penup()
    t.goto(x, y)
    t.dot(10)

def place_emoji(key):
    index = int(key) - 1  # Converting the key to an index (1-0 become 0-9)
    if 0 <= index < len(emojis):
        x, y = random.choice(dot_positions)
        draw_dot(x, y)
        t.penup()
        t.goto(x, y - 20)  # Positioning the emoji just below the dot
        t.write(emojis[index], align="center", font=("Arial", 20, "normal"))

# Setting up screen
screen = turtle.Screen()
screen.bgcolor("green")

# Creating turtle object
t = turtle.Turtle()
t.speed(5)

# Drawing circles
draw_circle(t, 150)  # Outer circle
draw_circle(t, 100)  # Middle circle
draw_circle(t, 50)   # Inner circle

dot_positions = []

# Drawing the inner symbols and dots
for angle in range(0, 360, 30):  # There are 12 sections
    draw_inner_pattern(t, angle, 100)
    dot_positions.append(t.pos())  # Store the position of the dot for later interaction
    draw_dot(*t.pos())

# Defining emojis for each keyboard letter (10 in total)
emojis = ["🐶", "🐱", "🦁", "🐵", "🐦", "🌻", "🍄", "🌊", "🌲", "🌹"]

# Key bindings
screen.onkey(lambda: place_emoji("1"), "1")
screen.onkey(lambda: place_emoji("2"), "2")
screen.onkey(lambda: place_emoji("3"), "3")
screen.onkey(lambda: place_emoji("4"), "4")
screen.onkey(lambda: place_emoji("5"), "5")
screen.onkey(lambda: place_emoji("6"), "6")
screen.onkey(lambda: place_emoji("7"), "7")
screen.onkey(lambda: place_emoji("8"), "8")
screen.onkey(lambda: place_emoji("9"), "9")
screen.onkey(lambda: place_emoji("0"), "0")

# Hideing turtle and display
t.hideturtle()
screen.listen()
screen.mainloop()

