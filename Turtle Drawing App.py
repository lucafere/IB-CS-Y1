import turtle
import math
screen = turtle.Screen()
turtle.setup(600,600)
screen.title("Turtle Drawing App")
screen.bgcolor("white")
pointer = turtle.Turtle()
pointer.speed(0)
pointer.hideturtle()
points=[]
pointer.penup()
print('Press: ')
print('* "r" for red')
print('* "g" for green')
print('* "b" for blue')
print('* "z" for black')
print('* "h" to put up pen')
print('* "s" to put down pen')

def distance (p1,p2):
   return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def dots(x,y):
    pointer.goto(x,y)
    pointer.dot(10)
    points.append((x, y))
    pointer.pendown()
    fill()
    
def fill():
   if len(points) > 2 and distance(points[0],points[-1])<20:
        pointer.begin_fill()
        for p in points:
            pointer.goto(p)
        pointer.goto(points[0])
        pointer.end_fill()
        if len(points)== 4:
           print("You made a triangle!")
        elif len(points)==5:
           print("You made a quadrilateral!")
        points.clear()
        pointer.penup()     

def g():
    pointer.color("green")
def r():
    pointer.color("red")
def b():
    pointer.color("blue")
def z():
    pointer.color("black")
def h():
    pointer.penup()
def s():
    pointer.pendown()
def c():
    pointer.clear()


    
screen.listen()
screen.onclick(dots)
screen.onkey(g,"g")
screen.onkey(r,"r")
screen.onkey(b,"b")
screen.onkey(z,"z")
screen.onkey(s,"s")
screen.onkey(h,"h")
screen.onkey(c,"c")
screen.mainloop()

