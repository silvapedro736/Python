from Tkinter import *



def wMainCallBack():

    wMain = Tk()
    #------------------------------------------------------------------------------
    def loginCallBack():
        #--------------------------------------------------------------------------
        def loginnCallBack():

            print "HEY"
        #--------------------------------------------------------------------------
        def signupCallBack():

            print "Hey"
        #--------------------------------------------------------------------------
        def backCallBack():

            wLogin.destroy()
            wMainCallBack()
    #--------------------------------------------------------------------------
    
        wMain.destroy()
    
        wLogin = Tk()

        font = "times", 25, "bold"
        lTitle = Label(wLogin, text = "Login", relief = RAISED, bd = 0, font = font)
        lTitle.place(x = 75, y = 45, width = 250, height = 40)

        lUsername = Label(wLogin, text="Username:")
        lUsername.place(x = 90, y = 90)
    
        eUsername = Entry(wLogin, bd =5)
        eUsername.place(x = 161, y = 90)
    
        lPassword = Label(wLogin, text="Password:")
        lPassword.place(x = 90, y = 120)
    
        ePassword = Entry(wLogin, bd =5)
        ePassword.place(x = 161, y = 120)

        bLogin = Button(wLogin, text ="Login", command = loginCallBack)
        bLogin.place(x = 137, y = 165)
    
        bSignup= Button(wLogin, text ="SignUp", command = signupCallBack)
        bSignup.place(x = 197, y = 165)
    
        bBack = Button(wLogin, text ="Back", command = backCallBack)
        bBack.place(x = 167, y = 210)

    
        wLogin.minsize(width = 400, height = 300)
        wLogin.maxsize(width = 400, height = 300)
        wLogin.title("Login")
        wLogin.mainloop()
    #-----------------------------------------------------------------------------------
    def helpCallBack():
        wMain.destroy()
    
        wHelp = Tk()

        wHelp.minsize(width = 0, height = 0)
        wHelp.maxsize(width = 0, height = 0)
        wHelp.title("Help!")
        wHelp.mainloop()
    #-----------------------------------------------------------------------------------
    def exitCallBack():
        wMain.destroy()

#---------------------------------------------------------------------------------------
    
    bLogin = Button(wMain, text = "Login", command = loginCallBack) 
    bLogin.place(x = 115, y = 140, width = 170)

    bHelp = Button(wMain, text = "Help", command = helpCallBack)
    bHelp.place(x = 115, y = 170, width = 170)

    bExit = Button(wMain, text = "EXIT", command = exitCallBack, fg = "red")
    bExit.place(x = 115, y = 200, width = 170)

    font = "times", 30, "bold"
    lTitle = Label(wMain, text = "Messages", relief = RAISED, bd = 0, font = font)
    lTitle.place(x = 75, y = 60, width = 250, height = 40)


    wMain.minsize(width = 400, height = 300)
    wMain.maxsize(width = 400, height = 300)
    wMain.title("Main Menu")
    wMain.mainloop()

wMainCallBack()
