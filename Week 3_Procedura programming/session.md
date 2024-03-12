## Hr 1 - Introducing turtle python

Learning objectives: learn how to use functions, variables, and parameters in Python, specifically with the Turtle graphics library, to draw simple shapes.

Setting Up Turtle Graphics

1. Open your Python IDE (Integrated Development Environment) or editor where you write Python code. In this case VSCode

2. Open a Python editor and type the following code:

```python
import turtle as t
screen = t.Screen()
pen = t.Turtle()
```

`import turtle as t` brings the Turtle library into our program, allowing us to use its functions.

Variables `screen` and `pen` represent the Turtle screen and the Turtle object, respectively.

3. Drawing with Turtle

Circle drawing 
```python
`pen.circle(50)`
```

`circle` is a function and `50` is a parameter specifying the radius of the circle in pixels.

4. Moving the turtle

```python
pen.penup()
pen.goto(150, 0)
pen.pendown()
pen.circle(50)
```

`penup()` and `pendown()` control whether the Turtle draws a line as it moves. `goto(150, 0)` moves the Turtle to a new position, where `(150, 0)` are parameters for the new coordinates

5. Closing the graphics window

```python
screen.exitonclick()
```

In event-driven programming `exitonclick()` keeps the window open until we click inside it. This shows how programs can react to user actions.

## Hr2 - Planning an interactive calendar

Customization Challenge

* Change Circle Sizes:
        Try changing the `50` in `pen.circle(50)` to other numbers to see how the size of the circle changes.

* Move Turtle to New Positions:
        Experiment with different values in `pen.goto(x, y)` to move the Turtle to various positions on the screen.

* Experiment with Colors:
        Before drawing a circle, set the pen's color with `pen.color('color_name')`. 
        Replace `'color_name'` with colors like `'blue', 'red', or 'green'`.
        Change the background color of the screen with `screen.bgcolor('color_name')`.

* Save and Run Your Program:
        After making your changes, save your Python file and run it. 
        Watch how the Turtle draws your design on the screen. 
        Experiment with different values and colors to create a unique drawing.

Use cases for our calendars
[here](https://docs.google.com/document/d/1CWoNWtTwpYgm09jLwFJCRJTY1TjjMK4DWeTDQ5Ppc8Q/edit)

## Hr 3

* Complete use cases using the problem-solving stages, which you can find here
* Complete your journals and submit them using the assignment link called journal progress
* Read the following article: https://criticallyconsciouscomputing.org/algorithms

Focus on sections 

1)  Key ideas and
2) Algorithm design and implementation sections