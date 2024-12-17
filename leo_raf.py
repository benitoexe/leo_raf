import turtle
import random

#two turtle objects
leo = turtle.Turtle()
raphael = turtle.Turtle()

#function to draw random side and color shape w/ skips
def random_shape(t, sides):
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    #random colors
    t.color(random.choice(colors)) 
    #calculates angles for the shape
    angle = 360/sides

    for i in range(sides):
        #randomize side lengths 
        t.forward(random.randint(50, 150)) 
        t.left(angle)
        #20% chance of skips 
        if random.random() < 0.2:  
            t.penup()
            #randomize skip lengths
            t.forward(random.randint(20, 50))
            t.pendown()
#draw shape using leo   
random_shape(leo, 5)
leo.penup()
leo.goto(-200, 0) 
leo.pendown()
#draw another shape using leo
random_shape(leo, 7) 

#star function :)
def interesting_shape(t):
    t.color("blue")
    for i in range(5):
        t.forward(100)
        t.right(144)

#draw stars with raphael and leo
raphael.penup()
raphael.goto(200, 100)
raphael.pendown()
interesting_shape(raphael)

leo.penup()
leo.goto(-200, -100) 
leo.pendown()
interesting_shape(leo)

#hide away both ninja turtles
leo.hideturtle()
raphael.hideturtle()

