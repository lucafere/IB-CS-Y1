import time
import datetime
print ("Todays date:", datetime.date.today())
dob = input("Type your date of birth (YYYY-MM-DD) ")
tday = datetime.date.today()
tdayy = tday.isoformat().split("-")
dobb = dob.split("-")
if int(tdayy[1]) > int(dobb[1]):
    if int(tdayy[2]) >= int(dobb[2]):
        years = int(tdayy[0]) - int(dobb[0])
        months = int(tdayy[1]) - int(dobb[1])
        days = int(tdayy[2]) - int(dobb[2])
    elif int(tdayy[2]) < int(dobb[2]):
        years = int(tdayy[0]) - int(dobb[0])
        months = int(tdayy[1]) - int(dobb[1]) - 1
        days = int(tdayy[2]) - int(dobb[2]) + 30
if int(tdayy[1]) == int(dobb[1]):
    if int(tdayy[2]) >= int(dobb[2]):
        years = int(tdayy[0]) - int(dobb[0])
        months = int(tdayy[1]) - int(dobb[1])
        days = int(tdayy[2]) - int(dobb[2])
    elif int(tdayy[2]) < int(dobb[2]):
        years = int(tdayy[0]) - int(dobb[0]) - 1
        months = int(tdayy[1]) - int(dobb[1]) + 11
        days = int(tdayy[2]) - int(dobb[2]) + 30
if int(tdayy[1]) < int(dobb[1]):
    if int(tdayy[2]) >= int(dobb[2]):
        years = int(tdayy[0]) - int(dobb[0]) - 1
        months = abs(int(tdayy[1]) - int(dobb[1]))
        days = int(tdayy[2]) - int(dobb[2])
    elif int(tdayy[2]) < int(dobb[2]):
        years = int(tdayy[0]) - int(dobb[0]) - 1
        months = abs(int(tdayy[1]) - int(dobb[1]))
        days = int(tdayy[2]) - int(dobb[2]) + 30

    
print(
    f"{years} year{'s' if years != 1 else ''} "
    f"{months} month{'s' if months != 1 else ''} "
    f"and {days + 1} day{'s' if (days + 1) != 1 else ''} "
    "have passed since you were born"
)

trigger = input("Press enter to start timer")
if trigger == "":
    start = time.time()
    print("Timer has started...")
trigger2 = input("Press enter to stop timer")
if trigger2 == "":
    stop = time.time()
elapsed = stop - start
print("Time elapsed was:",round(elapsed, 2),"seconds")







