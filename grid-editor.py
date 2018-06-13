import turtle, time , random
from settings import *

##screen = turtle.Screen()
##screen.setup(700,700)
##screen.bgcolor("lightgray")
##screen.tracer(0)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.pencolor("black")
        self.shape("square")
        self.shapesize(tile_size / 20)
        self.fillcolor("lightgray")
        self.speed(0)
        self.setpos(-280, 280)
     
pen = Pen()
pen2 = Pen()
grid = []
walls = []
for i in range(height):
    for i in range(width):
        pen.stamp()
        grid.append(pen.pos())
        pen.forward(tile_size)
    pen.back(tile_size * width)
    pen.right(90)
    pen.forward(tile_size)
    pen.left(90)
    pen.hideturtle()
    
def clicked(x ,y ):
    pen2.speed(0)
    x  =  int(tile_size*round(x/tile_size))
    y = int(tile_size*round(y/tile_size))
    pen2.goto(x,y)
    if (x,y) in grid:
        pen2.showturtle()
        if (x,y) not in walls:
            #print("Added new wall")
            pen2.color("black")
            pen2.fillcolor("brown")
            pen2.shape("square")
            pen2.stamp()
            walls.append((x,y))
        elif (x,y) in walls:
            #print("Removed wall")
            pen2.fillcolor("lightgray")
            pen2.stamp()
            walls.remove((x,y))      
    else:
        print("Click on the grid")


#-- print(walls) for copy
def print_walls():
    print(walls)

#-- clear the screen
def delete_all():
    pen2.speed(1)
    pen2.clearstamps()
    


#turtle.onkey(snake.right,"Right")
def main():
    turtle.listen()
    turtle.onkey(print_walls,"p")
    turtle.onkey(delete_all,"d")
    turtle.onscreenclick(clicked)
    turtle.mainloop()
if __name__ == "__main__":
    main()
    



    
