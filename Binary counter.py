b = input("Type binary code: ")
c = 0
m = 0
p = 0
pmax = 0
for x in b:
    p+=1
    if x == "1":
        c += 1
    else:
        if c>m:
            m = c
            pmax = p - m
        c = 0
        
if c > m:
    m = c
    pmax = p - m + 1   
        

print("The longst sequence of 1s is", m, "and it started in",pmax)
