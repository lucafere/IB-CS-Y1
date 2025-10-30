from tkinter import *
root = Tk()
root.title('New Widgets')
root.geometry('450x700+10+10')

# Variables
v = IntVar()
v1 = IntVar()

var1=IntVar()
var2=IntVar()
var3=IntVar()

# Function

    
    
# Widgets

## Label Widgets
## Button Widgets
## Entry Widgets

## Frame Widget

l1=Label(root, text="Label 1").pack()
separator = Frame(height=20, bd=1, relief=SUNKEN).pack(fill=X, padx=5, pady=5)
l2=Label(root, text="Label 2").pack()

# The frame widget can be used as a place holder for video overlays and other external processes.


## Checkbutton Widget
separator = Frame(height=20, bd=1, relief=SUNKEN).pack(fill=X, padx=5, pady=5)
c1 = Checkbutton(root, text="First Option", variable=var1).pack()
c2 = Checkbutton(root, text="Second Option", variable=var2).pack()
c3 = Checkbutton(root, text="Third Option", variable=var3).pack()
# By default, the variable is set to 1 if the button is selected, and 0 otherwise.
# You can change these values using the onvalue and offvalue options.

## Radiobutton widgets

Radiobutton(root, text="One", variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="Two", variable=v, value=2).pack(anchor=W)

# If you need to get notified when the value changes, attach a command callback to each button.

separator = Frame(height=20, bd=1, relief=SUNKEN).pack(fill=X, padx=5, pady=5)

# To turn the above example into a “button box” rather than a set of radio buttons
Radiobutton(root, text="One", variable=v1, value=1, indicatoron=0).pack(anchor=W)
Radiobutton(root, text="Two", variable=v1, value=2, indicatoron=0).pack(anchor=W)


# To get a proper radio behavior, make sure to have all buttons in a group point to the same variable,
# and use the value option to specify what value each button represents

separator = Frame(height=20, bd=1, relief=SUNKEN).pack(fill=X, padx=5, pady=5)

## OptionMenu Widget

variable = StringVar()
variable.set("one") # default value
om = OptionMenu(root, variable, "one", "two", "three").pack()

# To get the selected option

def ok():
    print ("value is", variable.get())
   

button = Button(root, text="OK", command=ok).pack()

separator = Frame(height=20, bd=1, relief=SUNKEN).pack(fill=X, padx=5, pady=5)

## Scale Widget

v2=IntVar()

sw = Scale(root, variable=v2, from_=0, to=200, orient=HORIZONTAL).pack()

# To query the widget, call the get method:


def ok2():
    print (v2.get())
   
button = Button(root, text="OK", command=ok2).pack()

## Images Widget

# The PhotoImage class can read GIF and PGM/PPM images from files:

separator = Frame(height=20, bd=1, relief=SUNKEN).pack(fill=X, padx=5, pady=5)

photo = PhotoImage(file="python.gif")

labeli = Label(image=photo, width=300).pack()

separator = Frame(height=20, bd=1, relief=SUNKEN).pack(fill=X, padx=5, pady=5)


# Events
root.mainloop()
