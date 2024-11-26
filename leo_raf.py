import turtle
import random

leo = turtle.Turtle()
raphael = turtle.Turtle()

def random_shape(t, sides):
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    t.color(random.choice(colors)) 
    angle = 360/sides
    
    for i in range(sides):
        t.forward(random.randint(50, 150)) 
        t.left(angle)
        if random.random() < 0.3:  
            t.penup()
            t.forward(random.randint(20, 50))
            t.pendown()
    
random_shape(leo, 5)
leo.penup()
leo.goto(-200, 0) 
leo.pendown()
random_shape(leo, 7) 

def interesting_shape(t):
    t.color("blue")
    for i in range(5):
        t.forward(100)
        t.right(144)


raphael.penup()
raphael.goto(200, 100)
raphael.pendown()
interesting_shape(raphael)

leo.penup()
leo.goto(-200, -100) 
leo.pendown()
interesting_shape(leo)

leo.hideturtle()
raphael.hideturtle()

