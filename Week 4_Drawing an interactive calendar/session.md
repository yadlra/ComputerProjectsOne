## Hr 1 & 2 - Creating your interactive calendar 

Example: 
1. Open file mayan_calendar.py
2. Alternatively open this [external weblink to code](https://trinket.io/library/trinkets/74fb54454d) 

### Setting Up the Calendar Display

* Open your Python editor and begin a new file.

* We'll need a few tools from our Python toolbox. Type in:


```python
import turtle
import calendar
import datetime
```

Here, we're bringing in the `turtle` library for our graphics, the `calendar` module to generate calendar displays, and `datetime` to work with dates.

* Next, set up the screen where our calendar will appear:


    ```python
    screen = turtle.Screen()
    screen.title("Interactive Calendar")
    calendar_pen = turtle.Turtle()
    calendar_pen.hideturtle()
    ```


This code creates a screen titled "Interactive Calendar" and prepares a Turtle object, `calendar_pe`n, for drawing. 
We hide the turtle cursor because we won't be drawing in the traditional sense.

### Displaying the calendar 

Now, let's make our calendar come to life:

We need a function that draws the calendar for a specific month and year:


    ```python
    def draw_calendar(year, month):
        calendar_pen.clear()
        cal_text = calendar.month(year, month)
        calendar_pen.write(cal_text, align="center", font=("Courier", 10, "bold"))
    ```

This function, `draw_calendar`, clears any previous calendar displayed, generates the calendar text for the specified month and year, and writes it on the screen.

### Making the Calendar Interactive 

Let's add the magic - making your calendar respond to clicks:

Define a function to handle screen clicks, which will decide what month to display based on where you click:



    ```python
    def on_click(x, y):
        current_year = datetime.datetime.now().year
        month = int(x // 50) + 6  # This is an example; adjust based on your screen layout
        draw_calendar(current_year, month)

    screen.onclick(on_click)
    turtle.done()
    ```

Here, when you click on the screen, `on_click` calculates which month you're aiming for based on the click's x-coordinate. 
The calendar for that month and the current year is then drawn.

Hands-on Practice 

Your turn! Follow the steps we just covered to write your interactive calendar. Apply your interests as you filled out in the last session! 


### Group Activity 

Share your work with a partner. 
Discuss what enhancements you added and any challenges you faced. How did you solve them?