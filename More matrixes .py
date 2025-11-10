from random import *
mat = [
    [12, 45, 78, 91],
    [23, 56, 88, 99],
    [88, 67, 81, 73],
    [48, 59, 62, 88]
]
for x in mat:
    print(x)
def symmetric(mat):
    sym = "Yes"
    for x in range(len(mat)):
        for y in range(len(mat)):
            if mat[x][y]!=mat[y][x]:
                sym = "No"
    print(f"The matrix is symmetric: {sym}")

def mostfrequent(mat):
    numbers = []
    frequency = []
    count = 0
    for x in mat:
        for y in x:
            if y not in numbers:
                numbers.append(y)
                frequency.append(1)
            else:
                pos = numbers.index(y)
                frequency[pos] += 1
    mostpos = frequency.index(max(frequency))
    mostfreq = numbers[mostpos]
    for x in mat:
        for y in x:
            if y == mostfreq:
                count += 1
    print(f" The most frequent number is {mostfreq} and it appears in {count} times")


def paper1short():
    L = [1,2,3,4,5,6,7,8,9,10,11,12]
    ARRAY=[]
    temp=[]
    for x in L:
        temp.append(x)
        if len(temp) == 4:
            ARRAY.append(temp)
            temp = []
    for x in ARRAY:
        print(x)


array = []
def paper1():
    global array 
    passangers = []
    temp = []
    for x in range(210):
        passangers.append(randint(200,500))
    for x in passangers:
        temp.append(x)
        if len(temp) == 7:
            array.append(temp)
            temp = []
    for x in array:
        print(x)
        
    temp = []
    avpass = 0
    for x in array:
        for y in x:
            temp.append(y)
    avpass = round(sum(temp)/len(temp))
    print("Average amount of passangers per day:",avpass)
day = ""
def convert(j):
    global day
    if j == 0:
        day = "Monday"
    elif j == 1:
        day = "Tuesday"
    elif j == 2:
        day = "Wednesday"
    elif j == 3:
        day = "Thursday"
    elif j == 4:
        day = "Friday"
    elif j == 5:
        day = "Saturday"
    elif j == 6:
        day = "Sunday"

totalpass = 0      
def total(i):
    global array, day, totalpass
    temp=[]
    day = ""
    for x in array:
        temp.append(x[i])
    convert(i)
    totalpass = sum(temp)
    print(f"There was a total of {totalpass} passangers that took the train in {day} in the last 30 weeks")
        
def dayaverage():
    global array, totalpass
    laverage=[]
    for x in range(6):
        total(x)   
        average = totalpass/len(array)
        laverage.append(average)
    bestindex = laverage.index(max(laverage))
    bestaverage = max(laverage)
    convert(bestindex)
    print(f"The day with the highest average of passangers is {day} with and average of {round(bestaverage)} passangers")

def sales(a,b,c,d):
    array = mat =[
    [329, 476, 310, 343, 466, 402, 216],
    [403, 281, 353, 435, 397, 495, 463],
    [342, 200, 468, 234, 257, 339, 224],
    [260, 328, 474, 386, 314, 258, 350],
    [391, 331, 396, 314, 256, 454, 258],
    [473, 360, 289, 228, 448, 372, 381],
    [376, 295, 295, 210, 453, 347, 356],
    [329, 210, 280, 403, 351, 482, 212],
    [488, 380, 322, 391, 269, 315, 394],
    [414, 370, 480, 420, 383, 463, 487],
    [468, 467, 237, 311, 466, 277, 321],
    [282, 334, 343, 308, 282, 498, 326],
    [499, 275, 227, 258, 209, 233, 459],
    [208, 458, 419, 353, 275, 467, 315],
    [491, 279, 316, 359, 476, 281, 476],
    [277, 412, 323, 417, 386, 350, 348],
    [221, 484, 267, 245, 442, 492, 443],
    [422, 340, 481, 493, 243, 238, 239],
    [407, 426, 303, 321, 264, 386, 361],
    [361, 350, 399, 213, 271, 478, 355],
    [382, 328, 366, 244, 396, 340, 385],
    [484, 391, 348, 216, 370, 310, 398],
    [309, 297, 260, 229, 375, 223, 448],
    [363, 469, 448, 261, 267, 334, 448],
    [497, 476, 432, 447, 445, 350, 346],
    [441, 356, 277, 262, 432, 459, 432],
    [286, 322, 237, 363, 246, 424, 242],
    [465, 268, 452, 449, 500, 494, 474],
    [495, 499, 315, 429, 325, 395, 278],
    [478, 463, 487, 391, 258, 419, 212]
    ]
    week = [0,1,2,3,4]
    weekdays = []
    weekends = []
    fees = [7,10]
    for i in range(len(array)):
        for j in range(len(array[0])):
            if i >= a:
                if i == a and j >= b:
                    if j in week:
                        weekdays.append(array[i][j])
                    else:
                        weekends.append(array[i][j])
                elif i > a and i < c:
                    if j in week:
                        weekdays.append(array[i][j])
                    else:
                        weekends.append(array[i][j])
                elif i == c and j <= d:
                    if j in week:
                        weekdays.append(array[i][j])
                    else:
                        weekends.append(array[i][j])
                    
                    
                
    totalweek = sum(weekdays)*fees[0]
    totalends = sum(weekends)*fees[1]
    totalsales =  totalweek + totalends
    print(weekdays)
    print(weekends)
    print(f"Total revenew between those days: ${totalsales}")
                        
        
    
        
    


            
        
