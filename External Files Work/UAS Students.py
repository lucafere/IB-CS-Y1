##qbfile = open("qbdata.txt", "r")
##for aline in qbfile:
##    values = aline.split()
##    print('QB ', values[0], values[1], 'had a rating of ', values[10] )
##qbfile.close()

##infile = open("secondarystudents.text","r")
##aline = infile.readline()
##c=0
##while aline:
##    items = aline.split(",")
##    country = items[3].lower()
##    if country[:3] == "arg":
##        c+=1
##    aline = infile.readline()
##print(f"There are {c} Argentinians in UAS")
##infile.close()

from tkinter import *
from customtkinter import *

#Commands/second windows 

def v1():
    namewindow = Toplevel(window)
    namewindow.geometry("500x500+10+10")
    namewindow.title("Student Name Search Bar")
    namewindow.attributes("-topmost", True)

    tv1=StringVar()
    tv2=StringVar()

    def searchname():
        infile = open("secondarystudents.text","r")
        aline = infile.readline()
        while aline:
            items = aline.strip().split(",")
            name = items[1].lower()
            lastname = items[2].lower()
            if tv1.get().lower() == name and tv2.get().lower() == lastname:
                print("Name:",items[1])
                print("Last Name:",items[2])
                print("Nationality:",items[3])
                print("Date Of Birth:",items[4])  
                break
        
            aline = infile.readline()
        print("")
        print("--------------------------------------------------------------------------------")
        print("")
        infile.close()
          
    namewindow.grid_columnconfigure(0, weight=1)
    namewindow.grid_columnconfigure(1, weight=1)
    bb1=CTkLabel(namewindow, text="Type in Name (left box) and Lastname (right box)").grid(row=0, column=0, columnspan="2", pady=10)
    bb2=CTkEntry(namewindow, textvariable=tv1).grid(row=1, column=0, pady=10)
    bb3=CTkEntry(namewindow, textvariable=tv2).grid(row=1, column=1, pady=10)
    bb4=CTkButton(namewindow, text="Search", command=searchname).grid(row=2, column=0, columnspan="2", pady=10)

    
def v2():
    yearwindow = Toplevel(window)
    yearwindow.geometry("500x500+10+10")
    yearwindow.title("Year of Birth Search Bar")
    yearwindow.attributes("-topmost", True)

    tvv1=StringVar()

    def yearsearch():
        c=0
        infile = open("secondarystudents.text","r")
        aline = infile.readline()
        while aline:
            items = aline.strip().split(",")
            year = items[4].split("/")
            if len(year) == 3:
                if tvv1.get() == year[2]:
                    c+=1
                    print(items[1], items[2])
            else:
                aline = infile.readline()
            aline = infile.readline()
        
        print(f"Total amount of people born in {tvv1.get()}: {c}")
        print("")
        print("--------------------------------------------------------------------------------")
        print("")
        infile.close()

    yearwindow.grid_columnconfigure(0, weight=1)
    bbb1=CTkLabel(yearwindow, text="Type in the year of birth").grid(row=0, column=0, pady=10)
    bbb2=CTkEntry(yearwindow, textvariable=tvv1).grid(row=1, column=0, pady=10)
    bbb4=CTkButton(yearwindow, text="Search", command=yearsearch).grid(row=2, column=0, pady=10)



#Main Window

window = Tk()
window.geometry("500x500+10+10")
window.title("UAS Data Base")
window.attributes("-topmost", True)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
b1=CTkLabel(window, text="Welcome to UAS Student Data base").grid(row=0, column=0, columnspan="2", pady=10)
b2=CTkLabel(window, text="Choose an option:").grid(row=1, column=0, columnspan="2", pady=10)
b3=CTkButton(window, text="Search By Name", command=v1).grid(row=2, column=0, pady=10)
b4=CTkButton(window, text="Search By Year", command=v2).grid(row=2, column=1, pady=10)

    
