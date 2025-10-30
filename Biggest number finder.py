counter = 0
l = []
s = float("-inf")
ss = float("inf")
while counter < 10:
    num = int(input("Choose number: "))
    l.append(num)
    counter += 1
    for x in l:
        if x > s:
            s = x
    for x in l:
        if x < ss:
            ss = x
    
print("The biggest number is:",s, "and the smallest number is", ss)
        
            
        
        
