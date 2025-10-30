import random
w = 0
l = 0
u = 0
m = 0
g = 0
again = "yes"
print("Rock, Paper, Scissors!")
while again == "yes":
    print("Choose between rock, paper or scissors (any other value will be taken as scissors)")
    while g != 5:
        user = input("User: ")
        user = user.lower()
        if user == "rock":
            u = 1
        elif user == "paper":
            u = 2
        else:
            u = 3
        m = random.randint(1, 3)
        if m == 1:
            print("Machine: Rock")
        elif m == 2:
            print("Machine: Paper")
        else:
            print("Machine: Scissors")
            
        if m == 1 and u == 2 or m == 2 and u == 3 or m == 3 and u == 1:
            print ("You Won!")
            u = 0
            m = 0
            w += 1
            g += 1
            print(f"The current score is {w} vs {l}")
        elif m == u:
            print("Tie!")
            u = 0
            m = 0
            print(f"The current score is {w} vs {l}")
        else:
            print("Machine Won")
            u = 0
            m = 0
            l += 1
            g += 1
            print(f"The current score is {w} vs {l}")
    if w>l:
        print(f"You Won {w} to {l}!")
    else:
        print(f"You lost {w} to {l}, better luck next time")
    g = 0
    w = 0
    l = 0
    again = input("Would you like to play again? Yes or No: ")
    again = again.lower()
print("See you next time!")
