import turtle
turtle.setup(500,500)
screen = turtle.Screen()
screen.title("Turtle Challenge")
screen.bgcolor("white")
luca = turtle.Turtle()
luca.speed(1000)
n = 0
s = 0
#Square 
while n!=4:
    luca.forward(100)
    luca.left(90)
    n+=1
#Circle
luca.circle(50)
#Partial circle
luca.circle(50,180)

#Square with color
luca.fillcolor("red")
luca.begin_fill()
while s!=4:
    luca.forward(100)
    luca.left(90)
    s+=1
luca.end_fill()

#Italian Flag
luca.pencolor("grey")
luca.fillcolor("green")
luca.begin_fill()
luca.forward(70)
luca.left(90)
luca.forward(120)
luca.left(90)
luca.forward(70)
luca.left(90)
luca.forward(120)
luca.end_fill()
luca.left(90)
luca.forward(70)
luca.fillcolor("white")
luca.begin_fill()
luca.forward(70)
luca.left(90)
luca.forward(120)
luca.left(90)
luca.forward(70)
luca.left(90)
luca.forward(120)
luca.end_fill()
luca.left(90)
luca.forward(70)
luca.fillcolor("red")
luca.begin_fill()
luca.forward(70)
luca.left(90)
luca.forward(120)
luca.left(90)
luca.forward(70)
luca.left(90)
luca.forward(120)
luca.end_fill()

#Fish shape
luca.penup()
luca.circle(100,-180)
luca.pendown()
luca.circle(100,180)
luca.left(90)
luca.forward(200)
luca.right(135)
luca.forward(282.8427125)
luca.fillcolor("red")
luca.begin_fill()
luca.left(135)
luca.forward(200)
luca.left(135)
luca.forward(282.8427125/2)
luca.end_fill()
luca.forward(282.8427125/2)






        
