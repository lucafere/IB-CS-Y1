
tank = 0
while tank<=50:
    answer=int(input("How much fuel would you like to add?"))
    if answer + tank >50:
        print("Answer exceded tank capacity!")
    elif answer + tank == 50:
        print("Tank at max capacity")
        break
    else:
        tank=tank+answer
        print("Tank fuel added")
        print("Current fuel amount: ",tank)

