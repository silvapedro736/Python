#Login Window
from Tkinter import *
import tkMessageBox

users = ["silvapedro736", "admin"]
passwords = ["1234567890", "admin"]

login = Tk()
lUsername = Label(login, text="Username:")
lUsername.place(x = 9, y = 6)
eUsername = Entry(login, bd =5)
eUsername.place(x = 80, y = 1)
lPassword = Label(login, text="Password:")
lPassword.place(x = 9, y = 35)
ePassword = Entry(login, bd =5)
ePassword.place(x = 80, y = 35)

def loginCallBack():
    for i in range(len(users)):
        if eUsername.get() == str(users[i]) and ePassword.get() == str(passwords[i]):
            tkMessageBox.showinfo( "Login", "Welcome " + str(eUsername.get()))
            break

def signupCallBack():
    signup = Tk()

    print 'hey'
    print eUsername.get()
    
    signup.minsize(width = 250, height = 127)
    signup.maxsize(width = 250, height = 127)
    signup.title("SignUp")
    signup.mainloop()

                    
bLogin = Button(login, text ="Login", command = loginCallBack)
bLogin.place(x = 93, y = 70)
bSignup= Button(login, text ="SignUp", command = signupCallBack)
bSignup.place(x = 88, y = 95)


login.minsize(width = 250, height = 127)
login.maxsize(width = 250, height = 127)
login.title("Login")
login.mainloop()
