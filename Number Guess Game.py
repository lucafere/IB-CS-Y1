import random

a = int(input("Choose min: "))
b = int(input("Choose max: "))
n = random.randint(a, b)
guess = int(input("type number: "))
attempts = 0
while guess!= n:
    if guess>n:
        print("Too High")
    elif guess<n:
        print("Too Low")
    guess=int(input("type number: "))
    attempts = attempts + 1
else:
    print("Good game! The number was", n)
    print("Attempts:",attempts)
