import turtle

def fal_back():
    turtle.right(90)  
    turtle.forward(200)  

def walk():
    turtle.forward(200)
    turtle.left(90)

    fal_back()

walk()

turtle.done()


