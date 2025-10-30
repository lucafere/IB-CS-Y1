steps = 10000
days=0
while steps>0:
    days=days+1
    ask=int(input("Add number of steps: "))
    if ask <0:
        print("Invalid imput")
    else:
        steps-=ask
    if steps>0:
        print("Steps needed to reach goal:",steps)
    else:
        print("Goal Reached!")
        print("Days taken to reach goal:",days)



