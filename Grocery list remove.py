
repeat = "yes"

while repeat == "yes":
    l = []
    ans = input("Add itmes to list, write 'done' in order to finish list: ")
    while ans != "done":
        l.append(ans)
        ans = input("Add itmes to list, write 'done' in order to finish list: ")
        
    for item in l:
        print("*", item)


    r = input("Which item would you like to remove?(if none, type 'none'): ")
    while r != "none":
        rr = r.split()
        for x in rr:
            
            if x in l:
                l.remove(x) 
            else:
                print("Sorry! That item is not in your list")
        
        for item in l:
                print("*", item)
        r = input("Which item would you like to remove?(if none, type 'none'): ")
                
    print("Grocery list completed! Items remaining:")
    for item in l:
                print("*", item)

    repeat = input("Would you like to make a new list? Type 'yes' or 'no': ")
    
print("Thank you for using listmaker.com!")
        
