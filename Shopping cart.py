cart = input("Add item price (write 'done' to end shopping): ")
money = 0
item = 0
while cart != "done":
    if cart == "done":
        break
    
    else:
        cart = int(cart)
        if cart<0:
            print("Input Invalid")
            
        else:
            item = item + 1
            money = money + cart
            print("Total price: $", money)
        cart = input("Add item price: ")
print ("Shopping done, end price is: $", money,"and you have",item,"items")

