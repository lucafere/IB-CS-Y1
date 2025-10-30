seats = [
    [1, 0, 1, 1, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]
]

print(seats[0])
print(seats[1])
print(seats[2])
print(seats[3])
print(seats[4])
print(seats[5])
print(seats[6])
print(seats[7])

occupied = 0
empty = 0
for x in seats:
    for y in x:
        if y == 1:
            occupied+=1
        else:
            empty+=1

print(f"There are {occupied} occupied seats and {empty} empty seats out of 64 total seats")
row1 = 0
row2 = 0
row3 = 0
row4 = 0
row5 = 0
row6 = 0
row7 = 0
row8 = 0
maxrow = 0

currentseats = 0
for x in seats[0]:
    if x == 1:
        row1+=1
        if row1 > maxrow:
            maxrow = 1
    if x == 0:
        currentseats+=1
    else:
        currentseats = 0
    if currentseats == 3:
        print(f"3 people can sit together in row 1")

currentseats = 0 
for x in seats[1]:
    if x == 1:
        row2+=1
        if row2 > maxrow:
            maxrow = 2
    if x == 0:
        currentseats+=1
    else:
        currentseats = 0
    if currentseats == 3:
        print(f"3 people can sit together in row 2")

currentseats = 0  
for x in seats[2]:
    if x == 1:
        row3+=1
        if row3 > maxrow:
            maxrow = 3
    if x == 0:
        currentseats+=1
    else:
        currentseats = 0
    if currentseats == 3:
        print(f"3 people can sit together in row 3")
        
currentseats = 0
for x in seats[3]:
    if x == 1:
        row4+=1
        if row4 > maxrow:
            maxrow = 4
    if x == 0:
        currentseats+=1
    else:
        currentseats = 0
    if currentseats == 3:
        print(f"3 people can sit together in row 4")
        
currentseats = 0
for x in seats[4]:
    if x == 1:
        row5+=1
        if row5 > maxrow:
            maxrow = 5
    if x == 0:
        currentseats+=1
    else:
        currentseats = 0
    if currentseats == 3:
        print(f"3 people can sit together in row 5")
        
currentseats = 0
for x in seats[5]:
    if x == 1:
        row6+=1
        if row6 > maxrow:
            maxrow = 6
    if x == 0:
        currentseats+=1
    else:
        currentseats = 0
    if currentseats == 3:
        print(f"3 people can sit together in row 6")
        
currentseats = 0
for x in seats[6]:
    if x == 1:
        row7+=1
        if row7 > maxrow:
            maxrow = 7
    if x == 0:
        currentseats+=1
    else:
        currentseats = 0
    if currentseats == 3:
        print(f"3 people can sit together in row 7")
        
currentseats = 0
for x in seats[7]:
    if x == 1:
        row8+=1
        if row8 > maxrow:
            maxrow = 8
    if x == 0:
        currentseats+=1
    else:
        currentseats = 0
    if currentseats == 3:
        print(f"3 people can sit together in row 8")


print(f"People per row:\nRow 1: {row1}\nRow 2: {row2}\nRow 3: {row3}\nRow 4: {row4}\nRow 5: {row5}\nRow 6: {row6}\nRow 7: {row7}\nRow 8: {row8}")
print(f"The row with most people is row {maxrow}")
print("To find specific spots or search for group of empty seats use:")
print("* seat_status(row, column)")
print("* can_seat_together(group_size)")

def seat_status(row, col):
    if seats [row-1][col-1] == 1:
        print(f"Seat in row {row} and column {col} is busy")
    else:
        print(f"Seat in row {row} and column {col} is empty")

def can_seat_together(groupsize):
    emptyseats = 0
    maxseats = 0 
    for x in seats:
        emptyseats=0
        for y in x:
            if y == 0:
                emptyseats += 1
            else:
                if emptyseats > maxseats:
                    maxseats = emptyseats
                emptyseats = 0
                
    if emptyseats > maxseats:  
        maxseats = emptyseats

    if maxseats >= groupsize:
        print(f"{groupsize} people can sit together")
    else:
        print(f"{groupsize} people cannot sit together")
    
            
    
                    
    
