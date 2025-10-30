import turtle
import random
import math
screen = turtle.Screen()
turtle.setup(700,700)
screen.title("Turtle Drawing App")
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.color("white")
t.penup()
l=[]
ll=[]
p=0
m=0
g=0


def square():
   t.hideturtle()
   t.penup()
   t.goto(0,280)
   t.write("Welcome to guessing game!", font=("Arial",30, "italic"), align="center")
   t.goto(0,0)
   t.forward(250)
   t.left(90)
   t.pendown()
   t.forward(250)
   t.left(90)
   t.forward(500)
   t.left(90)
   t.forward(500)
   t.left(90)
   t.forward(500)
   t.left(90)
   t.forward(250)
   t.left(90)
   t.penup()

square()

def distance (p1,p2):
   return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
   
def game(x,y):
      global p, m, g
      t.goto(x,y)
      t.dot(5, "red")
      ll.append((x,y))
      z = random.randint(-250,250)
      k = random.randint(-250,250)
      t.showturtle()
      t.goto(z,k)
      l.append((z,k))
      if distance(l[0],ll[0])<100:
         p=3 
      elif distance(l[0],ll[0])<250:
         p=2
      else:
         p=1
      print(p)
      l.clear()
      ll.clear()
      m = m+1
      g += p

      if m == 5:
         answer = screen.textinput( f'You won {g} points!','Wanna play again? Type "Yes", or "No"').lower()
         if answer == "yes":
            t.clear()
            square()
            m = 0
            g = 0
         else:
            t.clear()
            t.hideturtle()
            t.goto(0,0)
            t.write("Thank you for playing!", align="center", font=("Arial", 40, "italic"))
      
         
         
screen.listen()
screen.onclick(game)
screen.mainloop()




    
