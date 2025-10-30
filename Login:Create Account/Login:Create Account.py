from tkinter import *
from customtkinter import *
import time
# ==============================CREATE ACCOUNT WINDOW ============================

def create_account_page():
    window0 = Toplevel(window)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width=600
    height=600
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window0.geometry(f'{width}x{height}+{x}+{y}')
    window0.title("Create account")
    window0.attributes("-topmost", True)

    username=StringVar()
    password=StringVar()
    question=StringVar()
    answer=StringVar()
    confirmation=StringVar()

    def saveaccount():
        u = username.get().strip()
        p = password.get().strip()
        q = question.get().strip()
        a = answer.get().strip()
        if u == "" or p == "" or q == "" or a == "":
                confirmation.set("Cannot leave empty slots")
                return
        if not q.endswith("?"):   
                          q += "?" 
        try:
              with open ("accounts.txt","r") as f:
                  
                  for line in f:
                      items = line.split(",")
                      if items[0] == username.get():
                          confirmation.set("Account already exists")
                          return
        except FileNotFoundError:
              pass  

        with open("accounts.txt", "a") as f:
              f.write(f"{u},{p},{q},{a.lower()}\n")
              confirmation.set("Account created succesfully!")

    def homepage():
        window0.destroy()
        try:
            if window1.winfo_exists() or window2.winfo_exists():
                window1.destroy()
                window2.destroy()
        except NameError:
            pass
        

                               

    p1=CTkLabel(window0, text="Create an account:")
    p2=CTkLabel(window0, text="Username:")
    p3=CTkEntry(window0, textvariable=username)
    p4=CTkLabel(window0, text="Password:")
    p5=CTkEntry(window0, textvariable=password, show="*")
    p6=CTkLabel(window0, text="Create security question:")
    p7=CTkEntry(window0, textvariable=question)
    p8=CTkLabel(window0, text="Answer:")
    p9=CTkEntry(window0, textvariable=answer)
    p10=CTkButton(window0, text="Create account", command=saveaccount)
    p11=CTkEntry(window0, textvariable=confirmation)
    p12=CTkButton(window0, text="Go back to home page", command=homepage)

    #Grid

    window0.grid_columnconfigure(0, weight=1)
    window0.grid_columnconfigure(1, weight=1)

    p1.grid(row=0, column=0, columnspan="2")
    p2.grid(row=1, column=0, pady=10, padx=10)
    p3.grid(row=1, column=1, pady=10, padx=10)
    p4.grid(row=2, column=0, pady=10, padx=10)
    p5.grid(row=2, column=1, pady=10, padx=10)
    p6.grid(row=3, column=0, pady=10, padx=10)
    p7.grid(row=3, column=1, pady=10, padx=10)
    p8.grid(row=4, column=0, pady=10, padx=10)
    p9.grid(row=4, column=1, pady=10, padx=10)
    p10.grid(row=5, column=0, columnspan="2", pady=10, padx=10)
    p11.grid(row=6, column=0, columnspan="2", pady=10, padx=10, sticky="ew")
    p12.grid(row=7, column=0, columnspan="2", pady=10, padx=10)

# ============================== LOGIN WINDOW ===================================
userdata=[]
def login_account_page():
    window1 = Toplevel(window)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width=600
    height=600
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window1.geometry(f'{width}x{height}+{x}+{y}')
    window1.title("Login Account")
    window1.attributes("-topmost", True)

    username=StringVar()
    password=StringVar()
    question=StringVar()
    answer=StringVar()
    allinfo=StringVar()
    loginconfirmation=StringVar()
    login2confirmation=StringVar()


    def login():
        try:
            with open ("accounts.txt","r") as f:
                for line in f:
                    data = line.strip().split(",")
                    if data[0] == username.get() and data[1] == password.get():
                        loginconfirmation.set("Correct!")
                        userdata.append(data[0])
                        userdata.append(data[1])
                        userdata.append(data[2])
                        userdata.append(data[3])
                        question.set(userdata[2])
                        print(userdata)
                        break
                        
                    else:
                        loginconfirmation.set("Something is wrong")
        except FileNotFoundError:
            loginconfirmation.set("Must create an account!!!")
    def login2():
        global userdata 
        if loginconfirmation.get() == "Correct!":   
            if answer.get().lower() == userdata[3]:
                login2confirmation.set("Correct!")
                allinfo.set("Welcome!")
            else:
                login2confirmation.set("Wrong answer")
        else:
            login2confirmation.set("Must have correct user and password")

    def enterapp():
         if loginconfirmation.get() == "Correct!" and login2confirmation.get() == "Correct!":
             saveword()
         else:
             allinfo.set("Missing info!")

    def quitapp():
         window.destroy()

    def homepage():
        global userdata
        userdata.clear()
        try:
            if window0.winfo_exists():
                window0.destroy()
            elif window2.winfo_exists():
                window2.destroy()
        except NameError:
            pass
        window1.destroy()
        
             
        
                    

    h1=CTkLabel(window1, text="Username:")
    h2=CTkEntry(window1, textvariable=username)
    h3=CTkLabel(window1, text="Password:")
    h4=CTkEntry(window1, textvariable=password, show="*")
    h5=CTkEntry(window1, textvariable=loginconfirmation)
    h6=CTkButton(window1, text="Login", command=login)
    h7=CTkLabel(window1, text="Security question:")
    h8=CTkEntry(window1, textvariable=question)
    h15=CTkLabel(window1, text="Answer:")
    h9=CTkEntry(window1, textvariable=answer)
    h10=CTkEntry(window1, textvariable=login2confirmation)
    h11=CTkButton(window1, text="Login 2", command=login2)
    h12=CTkEntry(window1, textvariable=allinfo)
    h13=CTkButton(window1, text="Enter App", command=enterapp)
    h14=CTkButton(window1, text="Quit", command=quitapp)
    h15=CTkButton(window1, text="Go back to home page", command=homepage)

    #Grid

    window1.grid_columnconfigure(0, weight=1)
    window1.grid_columnconfigure(1, weight=1)

    h1.grid(row=0, column=0, pady=10, padx=10)
    h2.grid(row=0, column=1, pady=10, padx=10)
    h3.grid(row=1, column=0, pady=10, padx=10)
    h4.grid(row=1, column=1, pady=10, padx=10)
    h5.grid(row=3, column=0, pady=10, padx=10, columnspan="2", sticky="ew")
    h6.grid(row=2, column=0, columnspan="2", padx=10, pady=10)
    h7.grid(row=4, column=0, pady=10, padx=10)
    h8.grid(row=4, column=1, pady=10, padx=10)
    h15.grid(row=5, column=0, pady=10, padx=10)
    h9.grid(row=5, column=1, pady=10, padx=10)
    h10.grid(row=7, column=0, pady=10, padx=10, columnspan="2", sticky="ew")
    h11.grid(row=6, column=0, columnspan="2", padx=10, pady=10)
    h12.grid(row=8, column=0, columnspan="2", padx=10, pady=10)
    h13.grid(row=9, column=1, padx=10, pady=10)
    h14.grid(row=9, column=0, padx=10, pady=10)
    h15.grid(row=10, column=0, padx=10, pady=10, columnspan="2")

# ============================== SAVE INFO WINDOW ===================================


    def saveword():
        global userdata
        window2 = Toplevel(window)
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        width=600
        height=600
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window2.geometry(f'{width}x{height}+{x}+{y}')
        window2.title("UAS Data Base")
        window2.attributes("-topmost", True)

        word = StringVar()
        wordconfirmation= StringVar()

        def savewordbutton():
            with open("Savedwords.txt", "a") as userwords:
                if word.get() != "":
                    userwords.write(f"{userdata[0]},{word.get()}\n")
                    wordconfirmation.set("Word saved!")
                    window2.after(1000, lambda: wordconfirmation.set(""))


                    
                
        def showrecordsbutton():
            try:
                with open("Savedwords.txt", "r") as userwords:
                    for line in userwords:
                        items = line.strip().split(",")
                        if items[0] == userdata[0]:
                            print(items[1])
                        elif items[0] != userdata[0]: 
                            pass
                        else:
                            wordconfirmation.set("Sorry, no records saved")

            except FileNotFoundError:
                wordconfirmation.set("Sorry, no records saved")

        def eliminateword():
            found = False
            linestokeep=[]
            with open("Savedwords.txt", "r") as userwords:
                for line in userwords:
                    items = line.strip().split(",")
                    if not (items[0] == userdata[0] and word.get() == items[1]):
                        linestokeep.append(line)
                         
                    else:
                        found = True
                        wordconfirmation.set("Word not found")
                        window2.after(1000, lambda: wordconfirmation.set(""))
                        
            with open("Savedwords.txt", "w") as userwords:
                userwords.writelines(linestokeep)

            if found:
                wordconfirmation.set("Word deleted!")
                window2.after(1000, lambda: wordconfirmation.set(""))
            else:
                wordconfirmation.set("Word not found")
                window2.after(1000, lambda: wordconfirmation.set(""))
                
                
                             
        window2.grid_columnconfigure(0, weight=1)
        window2.grid_columnconfigure(1, weight=1)
        window2.grid_columnconfigure(2, weight=1)
       
        
        z1=CTkLabel(window2, text="Enter a word")
        z2=CTkEntry(window2, textvariable=word)
        z3=CTkButton(window2, text="Save", command=savewordbutton)
        z4=CTkButton(window2, text="Show records", command=showrecordsbutton)
        eliminate=CTkButton(window2, text="Delete word", command=eliminateword)
        wordconf=CTkEntry(window2, textvariable=wordconfirmation)
        z5=CTkButton(window2, text="Quit", command=quitapp)
     

        z1.grid(row=0, column=0, columnspan="3", pady=10)
        z2.grid(row=1, column=0, columnspan="3", pady=10)
        z3.grid(row=2, column=0, pady=10, padx=10)
        z4.grid(row=2, column=1, pady=10, padx=10)
        eliminate.grid(row=2, column=2, pady=10, padx=10)
        wordconf.grid(row=3, column=0, columnspan="3", sticky="ew", pady=10)
        z5.grid(row=4, column=0, columnspan="3", pady=10)

# ============================== MAIN WINDOW ===================================

window = Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width=600
height=600
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
window.geometry(f'{width}x{height}+{x}+{y}')
window.title("UAS Data Base")
window.attributes("-topmost", True)

def quitapp():
    window.destroy()

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
b1=CTkLabel(window, text="Welcome to Login").grid(row=0, column=0, columnspan="2", pady=10)
b2=CTkLabel(window, text="Choose an option:").grid(row=1, column=0, columnspan="2", pady=10)
b3=CTkButton(window, text="Create account", command=create_account_page).grid(row=2, column=0, pady=10)
b4=CTkButton(window, text="Login to account", command=login_account_page).grid(row=2, column=1, pady=10)
b5=CTkButton(window, text="Quit", command=quitapp).grid(row=3, column=0, columnspan="2", pady=10)


