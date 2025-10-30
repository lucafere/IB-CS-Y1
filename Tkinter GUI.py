from tkinter import *
from customtkinter import *

def loginpg(parent, username, password, question, answer):
      # create a window
      window=Toplevel(parent)
      window.title("Login to account")
      window.geometry("500x500+550+10")
      window.attributes("-topmost", True)

      # variables
      
      v1=StringVar()
      v2=StringVar()
      v3=StringVar()
      v4=StringVar()
      v5=StringVar()
      v6=StringVar()
      v7=StringVar()

      # functions

      def f1():
            if v1.get() == username and v2.get() == password:
                v3.set(question)
                v6.set("Correct!")
            else:
                v6.set("Something is wrong, try again")
                
      def f2():
            if v6.get() == "Correct!":
                if v4.get() == answer:
                    v7.set("Correct!")
                    v5.set("Login completed!")
                else:
                    v7.set("Not correct answer")
            else:
                  v7.set("Must have correct Username and Password")

            
                       
      def f3():
          window.destroy()
          window0.destroy()
          
      def f4():
            if v6.get()=="Correct!" and v7.get() == "Correct!":
                  window.destroy()
                  window0.destroy()
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
                        nonlocal p, m, g
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
                              t.goto(0,250)
                              t.write("Thank you for playing!", align="center", font=("Arial", 40, "italic"))
                              endanswer = screen.textinput("","Press enter to quit game")
                              if endanswer == "":
                                    screen.bye()
                              else:
                                    screen.bye()
             

                  screen.listen()
                  screen.onclick(game)
                  screen.mainloop()
            else:
                  v5.set("Missing Info!")

          
      # widgets
      h1=CTkLabel(window, text="Username:")
      h2=CTkEntry(window, textvariable=v1)
      h3=CTkLabel(window, text="Password:")
      h4=CTkEntry(window, textvariable=v2, show="*")
      h5=CTkEntry(window, textvariable=v6)
      h6=CTkButton(window, text="Login", command=f1)
      h7=CTkLabel(window, text="Security question:")
      h8=CTkEntry(window, textvariable=v3)
      h15=CTkLabel(window, text="Answer:")
      h9=CTkEntry(window, textvariable=v4)
      h10=CTkEntry(window, textvariable=v7)
      h11=CTkButton(window, text="Login 2", command=f2)
      h12=CTkEntry(window, textvariable=v5)
      h13=CTkButton(window, text="Enter App", command=f4)
      h14=CTkButton(window, text="Quit", command=f3)

      #Grid

      window.grid_columnconfigure(0, weight=1)
      window.grid_columnconfigure(1, weight=1)

      h1.grid(row=0, column=0, pady=10, padx=10)
      h2.grid(row=0, column=1, pady=10, padx=10)
      h3.grid(row=1, column=0, pady=10, padx=10)
      h4.grid(row=1, column=1, pady=10, padx=10)
      h5.grid(row=3, column=0, pady=10, padx=10, columnspan="2", sticky="ew")
      h6.grid(row=2, column=0, columnspan="2", padx=10, pady=10)
      h7.grid(row=4, column=0, pady=10, padx=10)
      h8.grid(row=4, column=1, pady=10, padx=10)
      h15.grid(row=5, column=0, pady=10, padx=10)
      h9.grid(row=5, column=1, pady=10, padx=10)
      h10.grid(row=7, column=0, pady=10, padx=10, columnspan="2", sticky="ew")
      h11.grid(row=6, column=0, columnspan="2", padx=10, pady=10)
      h12.grid(row=8, column=0, columnspan="2", padx=10, pady=10)
      h13.grid(row=9, column=1, padx=10, pady=10)
      h14.grid(row=9, column=0, padx=10, pady=10)
      

window0 = Tk()
window0.geometry("500x500+10+10")
window0.title("Create account")
window0.attributes("-topmost", True)

c1=StringVar()
c2=StringVar()
c3=StringVar()
c4=StringVar()
c5=StringVar()

def g1():
      global username, password, question, answer
      if c1.get() == "" or c2.get() == "" or c3.get() == "" or c4.get() == "":
            c5.set("Cannot leave empty slots")
      else:
            c5.set("Account Created!")
            username = c1.get()
            password = c2.get()
            question = c3.get()
            if not question.endswith("?"):   
              question += "?"
            answer = c4.get()
            loginpg(window0, username, password, question, answer)
      

p1=CTkLabel(window0, text="Create an account:")
p2=CTkLabel(window0, text="Username:")
p3=CTkEntry(window0, textvariable=c1)
p4=CTkLabel(window0, text="Password:")
p5=CTkEntry(window0, textvariable=c2, show="*")
p6=CTkLabel(window0, text="Create security question:")
p7=CTkEntry(window0, textvariable=c3)
p8=CTkLabel(window0, text="Answer:")
p9=CTkEntry(window0, textvariable=c4)
p10=CTkButton(window0, text="Create account", command=g1)
p11=CTkEntry(window0, textvariable=c5)

#Grid

window0.grid_columnconfigure(0, weight=1)
window0.grid_columnconfigure(1, weight=1)

p1.grid(row=0, column=0, columnspan="2")
p2.grid(row=1, column=0, pady=10, padx=10)
p3.grid(row=1, column=1, pady=10, padx=10)
p4.grid(row=2, column=0, pady=10, padx=10)
p5.grid(row=2, column=1, pady=10, padx=10)
p6.grid(row=3, column=0, pady=10, padx=10)
p7.grid(row=3, column=1, pady=10, padx=10)
p8.grid(row=4, column=0, pady=10, padx=10)
p9.grid(row=4, column=1, pady=10, padx=10)
p10.grid(row=5, column=0, columnspan="2", pady=10, padx=10)
p11.grid(row=6, column=0, columnspan="2", pady=10, padx=10, sticky="ew")
