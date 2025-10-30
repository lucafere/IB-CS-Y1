import time
import random
c = -10
u = -2
p = 0
r = 0
n = 1
n1 = 0
n2 = 0
n3 = 0
n4 = 0
again = "yes"
while again == "yes":
    c = -10
    u = -2
    p = 0
    r = 0
    n = 1
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    print("Rules:")
    print("* The machine will choose a random number between 1 and 10")
    print("* You will have 1 guess")
    print("* Play until you find the number or get +- 1 from it")
    print("* Once you win 5 times, game ends")
    difficulty = int(input("Choose dificulty 1, 2 or 3 (1-10, 1-100, 1-1000): "))
    #Si elegis difficulty 1 vas a tener que elegir los numeros manualmente
    #Si elegis difficulty 2 o 3, python lo hace por si solo 
    game = input("Press enter to start game")
    if game == "":
        start = time.time()
        if difficulty == 1:
            while p != 5:
                c = random.randint(1, 10)
                u = int(input("Guess the number chosen by the machine (1 - 10): "))
                print(f"You chose {u} and computer chose {c}")
                if u == c or u == c-1 or u == c+1:
                    p += 1
                    c = -10
                    u = -2
                    r += 1
                    print(f"Good! You won! Score is {p} you need {5 - p} more points to end the game")
                    if n == 1:
                        n1 = time.time()
                        n += 1
                    elif n == 2:
                        n2 = time.time()
                        n += 1
                    elif n == 3:
                        n3 = time.time()
                        n += 1
                    elif n == 4:
                        n4 = time.time()
                        n += 1      
                else:
                    print("Sorry, number not in range, try again")
                    r += 1

        elif difficulty == 2:
            while p != 5:
                c = random.randint(1, 100)
                u = random.randint(1, 100)
                print(f"You chose {u} and computer chose {c}")
                if u == c or u == c-1 or u == c+1 or u == c-2 or u == c+2:
                    p += 1
                    c = -10
                    u = -2
                    r += 1
                    print(f"Good! You won! Score is {p} you need {5 - p} more points to end the game")
                    if n == 1:
                        n1 = time.time()
                        n += 1
                    elif n == 2:
                        n2 = time.time()
                        n += 1
                    elif n == 3:
                        n3 = time.time()
                        n += 1
                    elif n == 4:
                        n4 = time.time()
                        n += 1
                else:
                    print("Sorry, number not in range, try again")
                    r += 1

        elif difficulty == 3:
            while p != 5:
                c = random.randint(1, 1000)
                u = random.randint(1, 1000)
                print(f"You chose {u} and computer chose {c}")
                if u == c or u == c-1 or u == c+1 or u == c-2 or u == c+2 or u == c-3 or u == c+3:
                    p += 1
                    c = -10
                    u = -2
                    r += 1
                    print(f"Good! You won! Score is {p} you need {5 - p} more points to end the game")
                    if n == 1:
                        n1 = time.time()
                        n += 1
                    elif n == 2:
                        n2 = time.time()
                        n += 1
                    elif n == 3:
                        n3 = time.time()
                        n += 1
                    elif n == 4:
                        n4 = time.time()
                        n += 1
                else:
                    print("Sorry, number not in range, try again")
                    r += 1
                
        end = time.time()
        elapsed = end - start
        print(f"Congratulations! You won 5 times, it only took you {round (elapsed, 1)}  seconds, ({round(elapsed / 60, 2)} minutes) and {r} rounds!")
        print(f"* 1st guess took you {round(n1 - start, 1)} seconds")
        print(f"* 2nd guess took you {round(n2 - start, 1)} seconds")
        print(f"* 3rd guess took you {round(n3 - start, 1)} seconds")
        print(f"* 4th guess took you {round(n4 - start, 1)} seconds")

        again = input("Would you like to play again? Yes or No: ").lower()
print("Thanks for playing!")
