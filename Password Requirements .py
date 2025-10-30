
print ("Must contain:")
print ("- At least 8 characters")
print ("- Upper case letter")
print ("- At least 1 digit")
print ("- At least a special character (! @ # $ % & *)")

a = 0
b = 0
c = 0
d = 0

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit = "0123456789"
sign = "! @ # $ % & *"

while a+b+c+d!=4:
    password = input("Insert Password: ")
    a = 0
    b = 0
    c = 0
    d = 0
    if len(password)>= 8:
        a=1
    else:
        print("Not 8 characters long")
    
    for x in password:
        if x in upper:
            b=1
    if b!=1:
        print("Password must conain upper")
   
    for x in password:
        if x in digit:
            c=1
    if c!=1:
        print("Password must contain digit")
        
    for x in password:
        if x in sign:
            d=1
    if d!=1:
        print("Password must contain sign")
            
    
    
    if a+b+c+d==4:
        print("Password valid")




        

    

