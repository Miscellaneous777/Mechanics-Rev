from tkinter import * # GUI commands!
import tkinter.ttk  as extra # Extra stuff for Tkinte
import sys # import system based functions
import time # import time based functions
from random import * # import randomisation based functions
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt # Import graphing based functions for Projectiles
matplotlib.use("TkAgg")

import database_manager as database # Import my own database file
import question_maker as QHelper # Import my own question maker
import graph_maker as graph # Import my own graph generator
import security as security # Import all security functions

# Written by Ben Dawson 13KNS - 2nd iteration of code due to messy code and a lack of comments

# To do -
# ~ Stop forgetting to put lambda in front of functions being run in buttons
# ~ Hash/Encrypt passwords - DONE!
# ~ Figure out how to pass variables between child classes 
# ~ Make first iteration of Projectiles tester - DONE!
# ~ Fix "Projectiles Tutorial" page - DONE!
# ~ Add testing pages so the teachers can set tests - DONE!
# ~ Add student testing pages so they can complete the tests
# ~ Finalise the styling throughout the whole program

class mainWindow(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self) # initialise
        sandbox = Frame(self) # "Sandbox" is where all frames will be switched around to and from
        sandbox.pack(fill = "both", expand = True) # Stretch all widgets to fill the sandbox frame, and allow widgets to expand                                      

        sandbox.grid_rowconfigure(0, weight=1)
        sandbox.grid_columnconfigure(0, weight=1)

        self.title("Mechanics Revision Program")
        self.geometry("1110x800+75+75")

        ###############################################################
        #         IMPORTANT VARIABLES FOR UI COLOURS AND FONTS        #
        ###############################################################

        self.TextColour = "#FFE082"#"#2E4053"
        self.BGColour = "#00ACC1" #"#17A589"
        self.ButtonColour = "#0097A7"
        
        self.fontTitle = ("Cambria", 20)
        self.fontBody = ("Courier", 11)
        self.fontButton = ("Cambria", 12)

        ###############################################################
        
        self.frames = {} #Place all frames into this Tuple - allows for easy window switching

        for item in (FirstWindow,LoginWindow,adminLogin,studentLogin,Projectiles_Q_Start,learnProj,adminProjectile,ProjectilesQ_Easy,Kinematics_Q_Start,learnKine,KinematicsQ_Easy_Weight,TestStart,TestInstructions):
            frame = item(sandbox, self) # store startup return in frame
            self.frames[item] = frame # insert the frame we've just gotten into the startup place in frames
            frame.grid(row=0,column=0,sticky="news")
    
        self.display_frame(FirstWindow) #Show the frame FirstWindow

    def display_frame(self, frameName): #useful function to raise any frame to the front of the program
        frame = self.frames[frameName] #Current frame is set to the requested one
        frame.tkraise() # Raise the requested frame to the top

    def get_page(self, page):
        return self.frames[page]

###############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OPENING WINDOW PAGES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###############################################################################################

class FirstWindow(Frame):

    def __init__(self, parent,desert):
        Frame.__init__(self,parent)

        self.desert = desert
 
        Frame.config(self, background = desert.BGColour)

        topPadding = Label(self,text = "", bg = desert.BGColour)
        topPadding.grid(padx=550,pady=125,column=0,row=0)
        
        #Main title
        menuTitle1 = Label(self,text="Mechanics Revision Program",font=desert.fontTitle,bg = desert.BGColour, fg = desert.TextColour)
        menuTitle1.grid(padx = 100,pady = 10)

        #Sub title
        menuSub1 = Label(self,text="Now in Alpha!",font = desert.fontBody,bg = desert.BGColour, fg = desert.TextColour)
        menuSub1.grid(pady = 0)

        #Login Button
        loginButton = Button(self,
                            text="Login",
                            width=16,
                            height=1,
                            command = lambda: desert.display_frame(LoginWindow),
                            font= ("Cambria", 16),
                            bg = desert.ButtonColour,
                            fg = desert.TextColour,
                            activebackground = desert.ButtonColour)
        loginButton.grid(padx=5,pady=5)

        #Quit Button
        QuitButton = Button(self,
                            text="Quit",
                            width=10,
                            height=1,
                            command = lambda: self.quitProgram(desert),
                            font = ("Cambria", 12),
                            bg = desert.ButtonColour,
                            fg = desert.TextColour,
                            activebackground = desert.ButtonColour)
        QuitButton.grid(padx=5,pady=10)

    def quitProgram(self,desert):
        desert.destroy()
        sys.exit()

###############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GENERAL LOGIN PAGES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###############################################################################################

class LoginWindow(Frame):

    def __init__(self,parent,desert):
        Frame.__init__(self,parent)

        self.desert = desert

        Frame.config(self, background = desert.BGColour) # setting background colour

        self.userInput = ""
        self.passInput = ""

        LoginWindow.grid_rowconfigure(parent,index = 0, weight=1, minsize = 800) # changing row and column sizes to centralise UI
        LoginWindow.grid_columnconfigure(parent,index = 0, weight=1, minsize = 1000)

        database_mech = database.DatabaseManipulate() # starting database
        database_mech.startup()

        topPadding = Label(self, text = "", bg = desert.BGColour)
        topPadding.grid(row=0,column = 1,columnspan=2,pady=125,padx=550)

        #title
        userFirstLabel = Label(self,text = "Login:", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        userFirstLabel.grid(row = 1, column= 1,columnspan= 2, pady= 5,padx= 525, sticky = S)

        #Username Label + Entry
        usernameLabel = Label(self,text = "Username:", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        usernameLabel.grid(row=2, column = 1,padx=12,pady=5,sticky = E)
        
        self.usernameEntry = Entry(self,width = 11, bg = desert.ButtonColour, font = desert.fontBody, fg = desert.TextColour)
        self.usernameEntry.grid(row=2,column=2,sticky = W)
        

        #Password Label + Entry
        passwordLabel = Label(self,text = "Password:", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        passwordLabel.grid(row=3, column = 1,padx=12,pady=5,sticky = E)

        self.passwordEntry = Entry(self,width = 11, show = ("*"), bg = desert.ButtonColour, font = desert.fontBody, fg = desert.TextColour)
        self.passwordEntry.grid(row=3,column=2,sticky = W)

        #confirm/deny entry label

        message2User = Label(self,text = "", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        message2User.grid(row=5,column = 1, columnspan = 3,padx=50,pady=5)

        # submit login button

        submitLogin = Button(self,text="Submit",width=11,height=1,
                             command = lambda: LoginWindow.verifyLogin(self,desert,message2User,database_mech),
                             font = desert.fontButton,
                             bg = desert.ButtonColour,
                             fg = desert.TextColour,
                             activebackground = desert.ButtonColour)
        submitLogin.grid(row=4,column = 1,columnspan = 1,pady=5,padx=5,sticky = E)

        


        #Cancel Login button (Return to main screen)
        cancelButton = Button(self, text = "Cancel",width=11,height=1,
                              command = lambda: desert.display_frame(FirstWindow),
                              font = desert.fontButton,
                              bg = desert.ButtonColour,
                              fg = desert.TextColour,
                              activebackground = desert.ButtonColour)
        cancelButton.grid(row=4, column = 2,pady=5,padx=5,sticky = W)


    def verifyLogin(self,desert,message2User,database_mech):

        adminValid = False
        studentValid = False

        adminPage = self.desert.get_page(adminLogin)

        self.userInput = self.usernameEntry.get() # Acquire the username and password entered
        self.passInput = self.passwordEntry.get()

        self.passInput = security.genHash(self.passInput) # Hash the password for checking

        StudentData = () # Create these two tuples for use later - need two, as entering teacher credentials provides
        TeacherData = () # a different level of access to student credentials

        StudentData = database_mech.StudentLoginCheck(self.userInput,self.passInput) #Get the relevant details from the database
        TeacherData = database_mech.AdminLoginCheck(self.userInput,self.passInput)

        if self.userInput == TeacherData[0]: # If the userInput is in the teacher table...
            if self.passInput == TeacherData[1]: # If the passInput is attached to that record...
                message2User.config(text="", bg=desert.BGColour)
                adminValid = True # Let them in with admin privileges
            else: # Otherwise...
                message2User.config(text="Incorrect Password!", bg="#ff6666") # Tell them it's wrong
        else: 
            if self.userInput == StudentData[0]: # If the userInput's in the student table...
                if self.passInput == StudentData[1]: # And if the passInput's attached to that record...
                    message2User.config(text="", bg=desert.BGColour)
                    studentValid = True # Let them in with student privileges
                else:
                    message2User.config(text="Incorrect Password!", bg="#ff6666") # Tell them the password's wrong
            else:
                message2User.config(text="Incorrect Username!", bg="#ff6666") # Tell them the username's wrong

        if adminValid or studentValid:
            self.usernameEntry.delete(0, "end") #Clear the entry boxes
            self.passwordEntry.delete(0, "end")
            adminPage.details = [self.userInput,self.passInput]
            print(adminPage.details)

        if adminValid == True:
            desert.display_frame(adminLogin) #Enter the admin area

        elif studentValid == True:
            desert.display_frame(studentLogin) # Enter the student area


###############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ADMIN GENERAL PAGES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###############################################################################################


class adminLogin(Frame):

    def __init__(self,parent,desert):
        Frame.__init__(self,parent)

        self.details = []

        self.desert = desert

        Frame.config(self, background = desert.BGColour)

        self.grid_columnconfigure(0, minsize = 25)
        self.grid_rowconfigure(0, minsize = 25)

        Columns = ["Student ID","First Name","Last Name","Password","Class ID"]

        loginDetails = self.desert.get_page(LoginWindow)

        username = loginDetails.usernameEntry.get()

        self.database_mech = database.DatabaseManipulate()

        #Main title
        menuTitle1 = Label(self,text="Welcome, "+username, font=desert.fontTitle,bg = desert.BGColour, fg = desert.TextColour)
        menuTitle1.grid(padx = 100,pady = 10,column = 2,row = 2)

        #Buttons
        logoutButton = Button(self,text = "← Logout",
                              command = lambda:desert.display_frame(LoginWindow),
                              font= desert.fontButton,
                              bg = desert.ButtonColour,
                              fg = desert.TextColour,
                              activebackground = desert.ButtonColour)
        logoutButton.grid(row = 1,column = 1)

        addStudentButton = Button(self, text = "Add Student",
                                  command = lambda: self.addBasicUser(desert),
                                  font= desert.fontButton,
                                  bg = desert.ButtonColour,
                                  fg = desert.TextColour,
                                  activebackground = desert.ButtonColour)
        addStudentButton.grid(row = 100, column =1)

        viewStudentButton = Button(self, text= "View Students",
                                   command = lambda: self.viewGeneral(desert,"Students","Student_ID",("First Name","Last Name", "Class ID", "Password")),
                                   font= desert.fontButton,
                                   bg = desert.ButtonColour,
                                   fg = desert.TextColour,
                                   activebackground = desert.ButtonColour)
        viewStudentButton.grid(row = 101, column = 1)

        addClassButton = Button(self,text = "Add a Class",
                                command = lambda: self.addClassData(desert),
                                font= desert.fontButton,
                                bg = desert.ButtonColour,
                                fg = desert.TextColour,
                                activebackground = desert.ButtonColour)
        addClassButton.grid(row=100, column = 2)

        viewClassButton = Button(self,text = "View Classes",
                                 command = lambda: self.viewGeneral(desert,"Class","Class_ID",("Teacher ID","Test ID",)),
                                 font= desert.fontButton,
                                bg = desert.ButtonColour,
                                fg = desert.TextColour,
                                activebackground = desert.ButtonColour)
        viewClassButton.grid(row=101, column = 2)

        addAdminButton = Button(self, text = "Add a Teacher",
                                command = lambda: self.addAdminUser(desert),
                                font= desert.fontButton,
                                bg = desert.ButtonColour,
                                fg = desert.TextColour,
                                activebackground = desert.ButtonColour)
        addAdminButton.grid(row = 100, column = 3)

        viewAdminButton = Button(self, text = "View all Teachers",
                                 command = lambda: self.viewGeneral(desert,"Teachers","Teacher_ID",("Teacher Title","Last Name", "Password")),
                                 font= desert.fontButton,
                                 bg = desert.ButtonColour,
                                 fg = desert.TextColour,
                                 activebackground = desert.ButtonColour)
        viewAdminButton.grid(row = 101, column = 3)

        makeMeGraphButton = Button(self, text = "Show a Projectile's Path",
                                   command = lambda: desert.display_frame(adminProjectile),
                                   font= desert.fontButton,
                                   bg = desert.ButtonColour,
                                   fg = desert.TextColour,
                                   activebackground = desert.ButtonColour)
        makeMeGraphButton.grid(row = 3, column = 2)

        makeATestButton = Button(self, text = "Create a Test",
                                 command = lambda: desert.display_frame(TestStart),
                                 font= desert.fontButton,
                                 bg = desert.ButtonColour,
                                 fg = desert.TextColour,
                                 activebackground = desert.ButtonColour)
        makeATestButton.grid(row = 4, column = 2)

    def addBasicUser(self,desert):
        
        creatingUser = Toplevel(desert)
        creatingUser.grab_set()
        creatingUser.geometry("500x250")
        creatingUser.title("Creating Student")

        creatingUser.config(bg = desert.BGColour)

        creatingUser.grid_columnconfigure(0, minsize = 20)
        creatingUser.grid_rowconfigure(0, minsize = 5)

        createLabel = Label(creatingUser, text = "Create user:", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        createLabel.grid(row=1,column=1,columnspan=2,pady=7.5)

        createUsernameLabel = Label(creatingUser, text = "Username/ID: ", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        createUsernameLabel.grid(row = 2,column = 1,sticky=W,pady=5,padx=5)

        createUsernameEntry = Entry(creatingUser, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        createUsernameEntry.grid(row = 2, column = 2)

        createFirstNameLabel = Label(creatingUser, text = "First Name: ", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        createFirstNameLabel.grid(row = 3,column = 1,sticky=W,pady=5,padx=5)

        createFirstNameEntry = Entry(creatingUser, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        createFirstNameEntry.grid(row = 3, column = 2)

        createLastNameLabel = Label(creatingUser, text = "Last Name: ", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        createLastNameLabel.grid(row = 4,column = 1,sticky=W,pady=5,padx=5)

        createLastNameEntry = Entry(creatingUser, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        createLastNameEntry.grid(row = 4, column = 2)

        createPasswordLabel = Label(creatingUser, text = "Password: ", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        createPasswordLabel.grid(row = 5,column = 1,sticky=W,pady=5,padx=5)

        createPasswordEntry = Entry(creatingUser, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        createPasswordEntry.grid(row = 5, column = 2)

        createClassIDLabel = Label(creatingUser, text = "Class ID: ", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        createClassIDLabel.grid(row = 6,column = 1,sticky=W,pady=5,padx=5)

        createClassIDEntry = Entry(creatingUser, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        createClassIDEntry.grid(row =6, column = 2)

        warningMessage = Label(creatingUser, text = "Please enter user \ndata to the left.", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour, anchor = "w", justify = "left")
        warningMessage.grid(column = 3,row = 2,sticky = W,rowspan=5, padx = 10)

        createEntryConfirm = Button(creatingUser, text = "Add User",
                                    command = lambda: self.confirmEntry(createUsernameEntry,createFirstNameEntry,createLastNameEntry,createPasswordEntry,createClassIDEntry,warningMessage),
                                    font= desert.fontButton,
                                    bg = desert.ButtonColour,
                                    fg = desert.TextColour,
                                    activebackground = desert.ButtonColour)
        createEntryConfirm.grid(row = 7,column=1)

        createEntryDeny = Button(creatingUser, text = "Go Back",
                                 command = lambda: self.cancelEntry(creatingUser),
                                 font= desert.fontButton,
                                 bg = desert.ButtonColour,
                                 fg = desert.TextColour,
                                 activebackground = desert.ButtonColour)
        createEntryDeny.grid(row=7,column=2)


    def confirmEntry(self,user,first,last,passw,cl_id,warningMessage):
        makeID = user.get()
        makeFirstName = first.get()
        makeLastName = last.get()
        makePassword = passw.get()
        makeClassID = cl_id.get()

        makePassword = security.genHash(makePassword)
        
        try:
            self.database_mech.addStudent(makeID,makeFirstName,makeLastName,makePassword,makeClassID)

            warningMessage.config(text="Success!\n\
Feel free to add another\n\
student or press\n\
\"Go Back\" to return to\n\
the menu")

            user.delete(0, "end")
            first.delete(0, "end")
            last.delete(0, "end")
            passw.delete(0, "end")
            cl_id.delete(0, "end")
        except:
            warningMessage.config(text="One of your inputs was\n\
wrong!\n\
If you're not sure about\n\
why, make sure to check\n\
that:\n\
 - The Student ID is\n\
   Unique\n\
 - The Class for the \n\
   Class ID exists")


    def addAdminUser(self,desert):
        
        creatingUser = Toplevel(desert)
        creatingUser.grab_set()
        creatingUser.geometry("500x235")
        creatingUser.title("Creating Admin")

        creatingUser.config(bg = desert.BGColour)

        creatingUser.grid_columnconfigure(0, minsize = 20)
        creatingUser.grid_rowconfigure(0, minsize = 5)

        createLabel = Label(creatingUser, text = "Create user:", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        createLabel.grid(row=1,column=1,columnspan=2,pady=7.5)

        createUsernameLabel = Label(creatingUser, text = "Username/ID: ", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour) # Username Label + Entry Box
        createUsernameLabel.grid(row = 2,column = 1,sticky=W,pady=5)

        createUsernameEntry = Entry(creatingUser, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        createUsernameEntry.grid(row = 2, column = 2)

        createTitleLabel = Label(creatingUser, text = "Title: ", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour) # Title Label + Entry Box
        createTitleLabel.grid(row = 3,column = 1,sticky=W,pady=5)

        createTitleEntry = Entry(creatingUser, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        createTitleEntry.grid(row = 3, column = 2)

        createLastNameLabel = Label(creatingUser, text = "Last Name: ", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour) # Last Name Label + Entry Box
        createLastNameLabel.grid(row = 4,column = 1,sticky=W,pady=5)

        createLastNameEntry = Entry(creatingUser, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        createLastNameEntry.grid(row = 4, column = 2)

        createPasswordLabel = Label(creatingUser, text = "Password: ", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour) # Password Label + Entry Box
        createPasswordLabel.grid(row = 5,column = 1,sticky=W,pady=5)

        createPasswordEntry = Entry(creatingUser, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        createPasswordEntry.grid(row = 5, column = 2)

        warningMessage = Label(creatingUser, text = "Please enter user data\nto the left.", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour, justify = "left") # Instructions Label 
        warningMessage.grid(column = 3,row = 2,sticky = NE,rowspan=6)

        createEntryConfirm = Button(creatingUser, text = "Add User", # Confirmation Button
                                    command = lambda: self.confirmAdminEntry(createUsernameEntry,createTitleEntry,createLastNameEntry,createPasswordEntry,warningMessage),
                                    font = desert.fontButton,
                                    bg = desert.ButtonColour,
                                    fg = desert.TextColour,
                                    activebackground = desert.ButtonColour)
        createEntryConfirm.grid(row = 7,column=1)

        createEntryDeny = Button(creatingUser, text = "Go Back", # Exit the toplevel button
                                 command = lambda: self.cancelEntry(creatingUser),
                                 font = desert.fontButton,
                                 bg = desert.ButtonColour,
                                 fg = desert.TextColour,
                                 activebackground = desert.ButtonColour)
        createEntryDeny.grid(row=7,column=2)


    def confirmAdminEntry(self,user,title,last,passw,warningMessage):
        makeID = user.get()
        makeTitle = title.get()
        makeLastName = last.get()
        makePassword = passw.get()

        makePassword = security.genHash(makePassword)
        
        try:
            self.database_mech.addTeacher(makeID,makeTitle,makeLastName,makePassword)

            warningMessage.config(text="Success!\n\
Feel free to add another\n\
student or press \n\
\"Go Back\" to return to \n\
the menu")

            user.delete(0, "end")
            title.delete(0, "end")
            last.delete(0, "end")
            passw.delete(0, "end")
        except:
            warningMessage.config(text="One of your inputs was\n\
wrong!\n\
If you're not sure about\n\
why, make sure to check\n\
that:\n\
 - The Student ID \n\
   is Unique\n\
 - The Class for the \n\
   Class ID exists")

    def addClassData(self,desert):
        
        creatingClass = Toplevel(desert)
        creatingClass.grab_set()
        creatingClass.geometry("500x220")
        creatingClass.title("Creating Class")

        creatingClass.grid_columnconfigure(0, minsize = 20)
        creatingClass.grid_rowconfigure(0, minsize = 5)

        creatingClass.config(bg= desert.BGColour)

        createLabel = Label(creatingClass, text = "Create Class:", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        createLabel.grid(row=1,column=1,columnspan=2,pady=7.5)
        

        createClassLabel = Label(creatingClass, text = "Class ID: ", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour) # Class ID Label + Entry Box
        createClassLabel.grid(row = 2,column = 1,sticky=W,pady=5)

        createClassEntry = Entry(creatingClass, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        createClassEntry.grid(row = 2, column = 2)
        

        createTeacherLabel = Label(creatingClass, text = "Teacher: ", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour) # Teacher ID Label + Entry Box
        createTeacherLabel.grid(row = 3,column = 1,sticky=W,pady=5)

        createTeacherEntry = Entry(creatingClass, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        createTeacherEntry.grid(row = 3, column = 2)
        

        createTestLabel = Label(creatingClass, text = "Test ID: ", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour) # Test ID Label + Entry Box
        createTestLabel.grid(row = 4,column = 1,sticky=W,pady=5)

        createTestEntry = Entry(creatingClass, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        createTestEntry.grid(row = 4, column = 2)
        

        warningMessage = Label(creatingClass, text = "Please enter class data to\n the left.", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour) # Instructions Label 
        warningMessage.grid(column = 3,row = 2,sticky = NE,rowspan=5)

        createEntryConfirm = Button(creatingClass, text = "Add Class", # Confirmation Button
                                    command = lambda: self.confirmClassEntry(createClassEntry,createTeacherEntry,createTestEntry,warningMessage),
                                    font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour,activebackground = desert.ButtonColour)
        createEntryConfirm.grid(row = 7,column=1)

        createEntryDeny = Button(creatingClass, text = "Go Back", # Exit the toplevel button
                                 command = lambda: self.cancelEntry(creatingClass),
                                 font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour,activebackground = desert.ButtonColour)
        createEntryDeny.grid(row=7,column=2)


    def confirmClassEntry(self,clas,teach,test,warningMessage):
        makeID = clas.get()
        makeTeach = teach.get()
        makeTest = test.get()
        try:
            self.database_mech.addClass(makeID,makeTeach,makeTest)

            warningMessage.config(text="Success!\n\
Feel free to add another\n\
class or press\n\
\"Go Back\" to return to\n\
the menu")

            clas.delete(0, "end")
            teach.delete(0, "end")
            test.delete(0, "end")
        except:
            warningMessage.config(text="One of your inputs was\n\
wrong!\n\
If you're not sure about\n\
why, make sure to check\n\
that:\n\
 - The Class ID \n\
   is Unique\n\
 - The Teacher for \n\
   the Teacher ID \n\
   exists")

    
    # This function is standardised, so it can be used wherever. Simply destroys the Toplevel object.   
    def cancelEntry(self,creatingUser):
        creatingUser.destroy()

    def delSelectedRecord(self,Table,TableName,ID):
        highlighted = Table.focus()
        focus_data = Table.item(highlighted)
        self.database_mech.delARecord(focus_data,TableName,ID)
        Table.delete(highlighted)

    def viewGeneral(self,desert,Table,FirstColumn,Columns):

        print(Table)

        viewGeneral = Toplevel(desert)
        viewGeneral.grab_set()
        viewGeneral.geometry("522x300")

        viewGeneral.config(bg=desert.BGColour)

        dbG = extra.Treeview(viewGeneral)
        dbG["columns"] = Columns
        dbG.heading("#0", text = FirstColumn)
        divisible = int(500/(len(Columns)+1))
        dbG.column("#0", width = divisible)
        extra.Style().configure("Treeview", background=desert.ButtonColour, foreground = "white", fieldbackground = desert.BGColour)

        for item in Columns:
            dbG.heading(item, text = item)
            dbG.column(item, width = divisible)

        scrollGeneral = extra.Scrollbar(viewGeneral, orient = "vertical")
        scrollGeneral.config(command = dbG.yview)

        Data = self.database_mech.allTableData(Table)
        
        for Item in Data:
            Item = Item + (" ",)
            dbG.insert("", "end", text = Item[0], values = Item[1:-1])
        dbG.grid(row=1,column=0,columnspan=3)

        dbG.config(yscrollcommand = scrollGeneral.set)
        scrollGeneral.grid(row=1,column = 4, sticky = N+S+E)

        Name_Table_Label = Label(viewGeneral, text = Table, bg = desert.BGColour, fg = desert.TextColour, font = desert.fontBody)
        Name_Table_Label.grid(row=0,column=0)

        DeleteEntry = Button(viewGeneral, text = "Delete Record",
                             command = lambda: self.delSelectedRecord(dbG, Table, FirstColumn),
                             font = desert.fontButton,
                             bg = desert.ButtonColour,
                             fg = desert.TextColour,
                             activebackground = desert.ButtonColour)
        DeleteEntry.grid(row=0,column=1)

        CloseWindow = Button(viewGeneral, text = "Close",
                             command = lambda: self.cancelEntry(viewGeneral),
                             font = desert.fontButton,
                             bg = desert.ButtonColour,
                             fg = desert.TextColour,
                             activebackground = desert.ButtonColour)
        CloseWindow.grid(row=0,column=2)


###############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ADMIN TESTING PAGES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###############################################################################################

class TestStart(Frame):

    def __init__(self,parent,desert):
        Frame.__init__(self,parent)

        Frame.config(self, background = desert.BGColour)

        self.database_mech = database.DatabaseManipulate()

        self.grid_columnconfigure(0, minsize = 25)
        self.grid_rowconfigure(0, minsize = 25)

        logoutButton = Button(self,text = "← Back", # Take us back to the main admin page
                              command = lambda: desert.display_frame(adminLogin),
                              font = desert.fontButton,
                              bg = desert.ButtonColour,
                              fg = desert.TextColour,
                              activebackground = desert.ButtonColour)
        logoutButton.grid(row = 0,column = 0)

        menuTitle1 = Label(self,text = "Test Creation Section",font=desert.fontTitle,bg = desert.BGColour, fg = desert.TextColour)
        menuTitle1.grid(row = 1, column = 1, columnspan = 5, padx = 100, pady = 10)

        instrButton = Button(self, text = "Instructions",
                             command = lambda: desert.display_frame(TestInstructions),
                             font=desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        instrButton.grid(row = 1, column = 6)

        TestLabel = Label(self, text = "Test Creation",font=desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        TestLabel.grid(row = 2, column = 1, columnspan = 2, padx = 75)

        TestIDLabel = Label(self, text = "Test ID: ",font=desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        TestIDLabel.grid(row = 3, column = 1, padx = 10, sticky = E)

        self.TestIDEntry = Entry(self,width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        self.TestIDEntry.grid(row = 3, column = 2, sticky = W)

        TestNameLabel = Label(self, text = "Test Name: ",font=desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        TestNameLabel.grid(row = 4, column = 1, padx = 10, sticky = E)

        self.TestNameEntry = Entry(self, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        self.TestNameEntry.grid(row = 4, column = 2, sticky = W)

        TestMaxMarkLabel = Label(self, text = "Max Mark: ",font=desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        TestMaxMarkLabel.grid(row = 5, column = 1, padx = 10, sticky = E)

        self.TestMarkEntry = Entry(self, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        self.TestMarkEntry.grid(row = 5, column = 2, sticky = W)

        warningMessage = Label(self, text = "\n\n\n",font=desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        warningMessage.grid(row = 7, column = 1, columnspan = 2, rowspan = 3)

        createButton = Button(self, text = "Create Test",
                              command = lambda: self.makeTest(warningMessage),
                              font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        createButton.grid(row = 6, column = 1, columnspan = 2)


        ######################################

        divide = Frame(self,height=350,width=2,bg=desert.ButtonColour) # Divider for the middle of the page
        divide.grid(row = 2, column = 3, rowspan = 9)

        ######################################
        

        QuestionLabel = Label(self, text = "Question Creation",font=desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        QuestionLabel.grid(row = 2, column = 4, columnspan = 2, padx = 125)

        QuestionIDLabel = Label(self, text = "Question ID: ",font=desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        QuestionIDLabel.grid(row = 3, column = 4, padx = 10, sticky = E)

        self.QuestionIDEntry = Entry(self, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        self.QuestionIDEntry.grid(row = 3, column = 5, sticky = W)

        QuestionTypeLabel = Label(self, text = "Question Type: ",font=desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        QuestionTypeLabel.grid(row = 4, column = 4, padx = 10, sticky = E)

        self.QuestionTypeEntry = Entry(self, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        self.QuestionTypeEntry.grid(row = 4, column = 5, sticky = W)

        QuestionDataLabel = Label(self, text = "Question Itself: ",font=desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        QuestionDataLabel.grid(row = 5, column = 4, padx = 10, sticky = E)

        self.QuestionDataEntry = Text(self, width = 45, height = 4, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        self.QuestionDataEntry.grid(row = 5 , column = 5, columnspan = 4, rowspan = 2, sticky = W)

        QuestionMarksLabel = Label(self, text = "Total Marks: ",font=desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        QuestionMarksLabel.grid(row = 7, column = 4, padx = 10, sticky = E)

        self.QuestionMarksEntry = Entry(self, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        self.QuestionMarksEntry.grid(row = 7, column = 5, sticky = W)

        QuestionAnswerLabel = Label(self, text = "Question Answer: ",font=desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        QuestionAnswerLabel.grid(row = 8, column = 4, padx = 10, sticky = E)

        self.QuestionAnswerEntry = Entry(self, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        self.QuestionAnswerEntry.grid(row = 8, column = 5, sticky = W)
        
        QuestionTestLabel = Label(self, text = "Test ID: ",font=desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        QuestionTestLabel.grid(row =  9, column = 4, padx = 10, sticky = E)

        self.QuestionTestEntry = Entry(self, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        self.QuestionTestEntry.grid(row = 9, column = 5, sticky = W)

        warningQuestion = Label(self, text = "\n\n\n",font=desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        warningQuestion.grid(row = 11, column = 4, columnspan = 2)

        createQuestButton = Button(self, text = "Create Question",
                              command = lambda: self.makeQuestion(warningQuestion),
                                   font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        createQuestButton.grid(row = 10, column = 4, columnspan = 2, pady = 10)
        

    def makeQuestion(self,warningQuestion):
        ID = self.QuestionIDEntry.get()
        Type = self.QuestionTypeEntry.get()
        Data = self.QuestionDataEntry.get("1.0",'end-1c')
        Marks = self.QuestionMarksEntry.get()
        TestID = self.QuestionTestEntry.get()
        Answer = self.QuestionAnswerEntry.get()

        try:
            self.database_mech.addQuestion(ID,Type,Data,Marks,TestID,Answer)

            warningQuestion.config(text = "Success! Test added.")

            self.QuestionIDEntry.delete(0, "end")
            self.QuestionDataEntry.delete(0, "end")
            self.QuestionMarksEntry.delete(0, "end")
            self.QuestionAnswerEntry.delete(0, "end")

        except:
             warningQuestion.config(text = "Question creation failed!\nPlease ensure that:\n - Test ID exists\n - Question ID is unique\n - Max Marks is a number!")
            


    def makeTest(self,warningMessage):
        ID = self.TestIDEntry.get()
        Name = self.TestNameEntry.get()
        Mark = self.TestMarkEntry.get()

        try:
            self.database_mech.addTest(ID,Name,Mark)

            warningMessage.config(text = "Success! Test added.")

            self.TestIDEntry.delete(0, "end")
            self.TestNameEntry.delete(0, "end")
            self.TestMarkEntry.delete(0, "end") 
        except:
            warningMessage.config(text = "Creation Failed!\nPlease make sure that:\n- Test ID is unique\n- Max Mark is a number!\n- All fields are filled in")
        
        

class TestInstructions(Frame):

    def __init__(self, parent, desert):
        Frame.__init__(self, parent)

        Frame.config(self, background = desert.BGColour)

        logoutButton = Button(self,text = "← Back", # Take us back to the main admin page
                              command = lambda: desert.display_frame(TestStart),
                              font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        logoutButton.grid(row = 0,column = 0)

        menuTitle1 = Label(self,text = "How to Create a Test",font=desert.fontTitle,bg = desert.BGColour, fg = desert.TextColour)
        menuTitle1.grid(row = 1, column = 1, columnspan = 2, padx = 100,pady = 10)

        firstLabel = Label(self, text = """To create a Test, you must first set it up using the boxes on the left.
Once this is done, you can add questions to it from the section on the right.
To change which test the questions are being added to, simply change the \"Test ID\" to that of the respective test.""",
                           font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        firstLabel.grid(row = 2, column = 1, columnspan = 2)

        
        


###############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ADMIN PROJ PAGES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###############################################################################################


class adminProjectile(Frame):

    def __init__(self,parent,desert):
        Frame.__init__(self,parent)

        Frame.config(self, background = desert.BGColour)

        xl = plt.figure()

        QGenYeah = QHelper.Projectiles()
        GraphGenYeah = graph.projGraph()

        logoutButton = Button(self,text = "← Back",
                              command = lambda: desert.display_frame(adminLogin),
                              font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        logoutButton.grid(row = 0,column = 0)

        menuTitle1 = Label(self,text = "Teacher Projectile Grapher",font=desert.fontTitle,bg = desert.BGColour, fg = desert.TextColour)
        menuTitle1.grid(row = 1, column = 1, columnspan = 2)

        subTitle1 = Label(self, text = "This page can be used by teachers in order to accurately show a projectile curve to the class.",
                          font=desert.fontBody,bg = desert.BGColour, fg = desert.TextColour)
        subTitle1.grid(row = 2, column = 1, columnspan = 2)

        angleTextLabel = Label(self, text = "Angle:",
                               font=desert.fontBody,bg = desert.BGColour, fg = desert.TextColour)
        angleTextLabel.grid(row = 3, column = 1)

        self.angleInputEntry = Entry(self, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        self.angleInputEntry.grid(row = 3, column = 2)

        velocityTextLabel = Label(self, text = "Velocity:", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        velocityTextLabel.grid(row = 4, column = 1)

        self.velocityInputEntry = Entry(self, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        self.velocityInputEntry.grid(row = 4, column = 2)

        showGraphButton = Button(self, text = "Show Graph",
                                 command = lambda: self.showGraph(QGenYeah,GraphGenYeah,xl),
                                 font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        showGraphButton.grid(row = 90, column = 1, columnspan = 2)

        clearGraphButton = Button(self, text = "Clear Graph",
                                  command = lambda: plt.gcf().clear(xl),
                                  font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        clearGraphButton.grid(row=100, column = 1, columnspan=2)

    def showGraph(self,QGenYeah,GraphGenYeah,xl):

        angle1 = self.angleInputEntry.get()
        angle1 = int(angle1)
        
        velocity1 = self.velocityInputEntry.get()
        velocity1 = int(velocity1)

        finalPoint, highPoint,timeTakenEnd = QGenYeah.simple_q_teach(angle1,velocity1)

        xl = GraphGenYeah.makeTeachGraph(xl,velocity1,angle1,finalPoint,timeTakenEnd,highPoint)

        canvas1 = FigureCanvasTkAgg(xl,self)
        canvas1.show()
        canvas1.get_tk_widget().grid(row=5, column=1, columnspan=2)

        
###############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~ GENERAL STUDENT PAGES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###############################################################################################

class studentLogin(Frame):

    def __init__(self,parent,desert):
        Frame.__init__(self,parent)

        StudentDatabase = database.DatabaseManipulate()
        username = "Student"

        Frame.config(self, background = desert.BGColour)

        StudentDatabase.b.execute("""SELECT Student_FirstName,Student_LastName,Class_ID FROM Students WHERE Student_ID = '{}'""".format(username))
        Logged_In_Data = StudentDatabase.b.fetchone()

        #Main title
        menuTitle1 = Label(self,text="Welcome, "+Logged_In_Data[0]+"!",font=desert.fontTitle,bg = desert.BGColour, fg = desert.TextColour)
        menuTitle1.grid(padx = 100,pady = 10,column=1,row=1)


        #Buttons

        ProjPractice =  Button(self,text = "Projectiles Revision",
                               command = lambda: desert.display_frame(Projectiles_Q_Start),
                               font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)

        ProjPractice.grid(row = 3, column = 1)

        SetTest = Button(self, text = "Teacher Set Tests",
                          command = lambda: print("NO PAGE FOUND"),
                          font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour) # PUT DISPLAY FRAME HERE!!!!!!!!

        SetTest.grid(row = 4, column = 1)

        KinePractice = Button(self, text = "Kinematics Practice",
                              command = lambda: desert.display_frame(Kinematics_Q_Start),
                              font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        KinePractice.grid(row = 2, column = 1)
        
        logoutButton = Button(self,text = "← Logout",
                              command = lambda: desert.display_frame(LoginWindow),
                              font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        logoutButton.grid(row = 0,column = 0)

###############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PROJECTILE PAGES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###############################################################################################

class Projectiles_Q_Start(Frame):

    def __init__(self, parent,desert):
        Frame.__init__(self,parent)

        Frame.config(self, background = desert.BGColour)

        topLabel = Label(self, text = "Projectiles Section",font=desert.fontTitle,bg = desert.BGColour, fg = desert.TextColour)
        topLabel.grid(column = 1, row = 1, columnspan = 2)

        expanLabel = Label(self, text = "Welcome to the Projectiles revision section! \n Please click any of the buttons below to access the corresponding section. ",
                           font=desert.fontBody,bg = desert.BGColour, fg = desert.TextColour)
        expanLabel.grid(column = 1, row = 2,columnspan = 2)

        ProjExpllabel = Label(self, text = "Projectiles Basic Explanation",
                              font=desert.fontBody,bg = desert.BGColour, fg = desert.TextColour)
        ProjExpllabel.grid(column = 1, row = 3)

        ProjExplButton = Button(self, text = "Learn!",
                                command = lambda: desert.display_frame(learnProj),
                                font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        ProjExplButton.grid(column = 2, row = 3)

        ProjBasicQLabel = Label(self, text = "Projectiles Easy Questions",
                                font=desert.fontBody,bg = desert.BGColour, fg = desert.TextColour)
        ProjBasicQLabel.grid(column = 1,row = 4)

        ProjBasicQButton = Button(self, text = "Learn!",
                                  command = lambda: desert.display_frame(ProjectilesQ_Easy),
                                  font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        ProjBasicQButton.grid(column = 2, row = 4)

        #Logout Button
        logoutButton = Button(self,text = "← Back",
                              command = lambda: desert.display_frame(studentLogin),
                              font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        logoutButton.grid(row = 0,column = 0)
        

class learnProj(Frame): # Projectile Explanation!

    def __init__(self,parent,desert):
        Frame.__init__(self,parent)

        Frame.config(self, background = desert.BGColour)

        logoutButton = Button(self,text = "← Back",
                              command = lambda: desert.display_frame(Projectiles_Q_Start),
                              font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        logoutButton.grid(row = 0,column = 0)

        titleLabel = Label(self, text = "Projectiles Explanation",font=desert.fontTitle,bg = desert.BGColour, fg = desert.TextColour)
        titleLabel.grid(row = 1, column = 1)

        firstExpLabel = Label(self, text = """Projectiles are by definition a single particle with no engine or power source attached.
Most simple projectiles questions will give you the intial velocity of the particle
- and also the angle it was launched at. 
From this, we must derive the individual parts of the velocity for the i and j directions
- this will allow us to figure out heights and distances much more easily.

Imagine a projectile (that experiences no air resistance) is
launched at a speed of \"U\" m/s and an angle of \"A\" degrees.

From this, we can figure out that the velocity in i's and j's is U = UcosAi + UsinAj
The only acceleration this particle can feel is from Gravity
- which means it's -9.81j, as gravity has no effect in the horizontal plane.
Therefore, to work out Velocity at any point we can combine these two equations to get:

V = UcosAi + (UsinA - 9.81t)j

Where \"t\" is the time at that point.

We can also derive an equation for Distance using similar techniques, remember SUVAT?

s = ut + 1/2at²

We can use this for our own equations to form:

S = UtcosAi + (UtSinA - 1/2(9.81t)²)j

To work out the final landing point of the projectile,
we can set the \"j\" part of the equation to 0, to simulate the floor,
and then solve it for \"t\".
We can then put this into the \"i\" section of the equation to find distance.
We can also halve that time to work out the time taken to get to the highest point,
and then use the j component of the distance equation to find the highest point.

The Simple Question generator on the next page expects answer to 2dp,
so make sure you're as accurate as you can be with your calculations!""",
                              font=desert.fontBody,bg = desert.BGColour, fg = desert.TextColour)
        firstExpLabel.grid(row = 2, column = 1)
        

class ProjectilesQ_Easy(Frame): # Projectile Easy Questions!

    def __init__(self,parent,desert):
        Frame.__init__(self,parent)

        Frame.config(self, background = desert.BGColour)

        logoutButton = Button(self,text = "← Back",
                              command = lambda: desert.display_frame(Projectiles_Q_Start),
                              font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        logoutButton.grid(row = 0,column = 0)

        f = plt.figure()

        QGen = QHelper.Projectiles()
        GraphGen = graph.projGraph()
        
        self.angle, self.velocity, self.finalpoint, self.highPoint, self.timeTakenEnd = 0,0,0,0,0
        self.visibleQ = ""
        self.answerNeeded = ""

        topLabel = Label(self, text = "Easy Question Generator",font=desert.fontTitle,bg = desert.BGColour, fg = desert.TextColour)
        topLabel.grid(column = 1, row = 0, columnspan = 2)

        self.explanationLabel = Label(self, text = self.visibleQ, font=desert.fontBody,bg = desert.BGColour, fg = desert.TextColour)
        self.explanationLabel.grid(column = 1, row = 1, columnspan = 2)

        self.ansRightWrong = Label(self, text = "", font=desert.fontBody,bg = desert.BGColour, fg = desert.TextColour)
        self.ansRightWrong.grid(column = 3, row = 1)

        angleLabel1 = Label(self, text = "Angle: ", font=desert.fontBody,bg = desert.BGColour, fg = desert.TextColour)
        angleLabel1.grid(row = 2, column = 1)

        self.angleLabel2 = Label(self, text = self.angle, font=desert.fontBody,bg = desert.BGColour, fg = desert.TextColour)
        self.angleLabel2.grid(row = 2, column = 2)

        velocityLabel1 = Label(self, text = "Velocity: ", font=desert.fontBody,bg = desert.BGColour, fg = desert.TextColour)
        velocityLabel1.grid(row = 3, column = 1)

        self.velocityLabel2 = Label(self, text = self.velocity, font=desert.fontBody,bg = desert.BGColour, fg = desert.TextColour)
        self.velocityLabel2.grid(row = 3, column = 2)

        self.answerNeededLabel = Label(self, text = self.answerNeeded, font=desert.fontBody,bg = desert.BGColour, fg = desert.TextColour)
        self.answerNeededLabel.grid(row=4, column = 1)

        self.answerNeededEntry = Entry(self, width = 11, font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        self.answerNeededEntry.grid(row = 4, column = 2)

        ansQButton = Button(self, text = "Submit!",
                            command = lambda: self.CheckAns(),
                            font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        ansQButton.grid(row = 98, column = 1, columnspan = 2)

        genQButton = Button(self, text = "Generate Question!",
                            command = lambda: self.showQ(QGen,GraphGen,f),
                            font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        genQButton.grid(row = 99, column = 1, columnspan = 2)

        clearGraphButton = Button(self, text = "Clear Graph",
                                  command = lambda: plt.gcf().clear(f),
                                  font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        clearGraphButton.grid(row=100, column = 1, columnspan=2)


    def showQ(self,QGen,GraphGen,f):

        self.ansRightWrong.config(text="") # Empty the right/wrong box

        self.answerNeededEntry.delete(0, "end") # Empty the entry box

        self.angle, self.velocity, self.finalPoint, self.highPoint, self.timeTakenEnd = QGen.simple_q() # create all the variables

        self.visibleQ = "A Projectile is launched at an angle of "+str(self.angle)+"° and at a velocity of "+str(self.velocity)+"m/s." # first part of the question

        self.angleLabel2.config(text = self.angle)
        self.velocityLabel2.config(text = self.velocity)

        ansReq = randint(1,3)

        if ansReq == 1:
            self.visibleQ = self.visibleQ + "\nFind how far the final landing point is from the launch point is, in metres, to 2dp."
            self.answerNeeded = "Final Landing Point"

        elif ansReq == 2:
            self.visibleQ = self.visibleQ + "\nFind the height of the highest point the projectile reaches, in metres, to 2dp."
            self.answerNeeded = "Highest Point"

        elif ansReq == 3:
            self.visibleQ = self.visibleQ + "\nFind how long the projectile took to reach the ground again, in seconds, to 2dp."
            self.answerNeeded = "Time Taken"

        self.answerNeededLabel.config(text = self.answerNeeded)
        self.explanationLabel.config(text = self.visibleQ)

        ############################################################
        
        f = GraphGen.makeGraph(f,self.velocity,self.angle,self.finalPoint,self.timeTakenEnd,self.highPoint)

        plt.tick_params(axis='both', labelleft='off', labelright='off', labelbottom='off')

        canvas = FigureCanvasTkAgg(f,self)
        canvas.show()
        canvas.get_tk_widget().grid(row=5, column=1, columnspan=2)

    def CheckAns(self):

        InputAns = self.answerNeededEntry.get()
        if InputAns == "": #Error handling - stops it from trying to convert a string to a float.
            InputAns = 0
        print("current values:",self.finalPoint,self.highPoint,self.timeTakenEnd)

        if self.answerNeeded == "Final Landing Point":
            if float(InputAns) == round(self.finalPoint,2):
                self.ansRightWrong.config(text = "Correct!")
                self.answerNeededEntry.delete(0, "end")
            else:
                self.ansRightWrong.config(text = "Wrong! :(\nPlease try again")

        elif self.answerNeeded == "Highest Point":
            if float(InputAns) == round(self.highPoint,2):
                self.ansRightWrong.config(text = "Correct!")
                self.answerNeededEntry.delete(0, "end")
            else:
                self.ansRightWrong.config(text = "Wrong! :(\nPlease try again")

        elif self.answerNeeded == "Time Taken":
            if float(InputAns) == round(self.timeTakenEnd,2):
                self.ansRightWrong.config(text = "Correct!")
                self.answerNeededEntry.delete(0, "end")
            else:
                self.ansRightWrong.config(text = "Wrong! :(\nPlease try again")
        
###############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ KINEMATICS PAGES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###############################################################################################
             
class Kinematics_Q_Start(Frame):

    def __init__(self, parent,desert):
        Frame.__init__(self,parent)

        Frame.config(self, bg = desert.BGColour)

        topLabel = Label(self, text = "Kinematics Section",font=desert.fontTitle,bg = desert.BGColour, fg = desert.TextColour)
        topLabel.grid(column = 1, row = 0, columnspan = 2)

        expanLabel = Label(self, text = "Welcome to the Kinematics revision section! \n Please click any of the buttons below to access the corresponding section. ",
                           font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        expanLabel.grid(column = 1, row = 1,columnspan = 2)

        KineExpllabel = Label(self, text = "Kinematics Basic Explanation",
                              font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        KineExpllabel.grid(column = 1, row = 2)

        KineExplButton = Button(self, text = "Learn!",
                                command = lambda: desert.display_frame(learnKine),
                                font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        KineExplButton.grid(column = 2, row = 2)

        KineBasicQLabel = Label(self, text = "Kinematics Easy Weight Questions",
                                font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        KineBasicQLabel.grid(column = 1,row = 3)

        KineBasicQButton = Button(self, text = "Learn!",
                                  command = lambda: desert.display_frame(KinematicsQ_Easy_Weight),
                                  font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        KineBasicQButton.grid(column = 2, row = 3)

        #Logout Button
        logoutButton = Button(self,text = "← Back",
                              command = lambda: desert.display_frame(studentLogin),
                              font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        logoutButton.grid(row = 0,column = 0)

class learnKine(Frame):  ########################## LEARNING KINEMATICS

    def __init__(self,parent,desert):
        Frame.__init__(self,parent)

        Frame.config(self, bg = desert.BGColour)

        logoutButton = Button(self,text = "← Back",
                              command = lambda: desert.display_frame(Kinematics_Q_Start),
                              font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        logoutButton.grid(row = 0,column = 0)


class KinematicsQ_Easy_Weight(Frame):  ################################# KINEMATICS QUESTIONS

    def __init__(self, parent,desert):
        Frame.__init__(self,parent)

        #Logout Button
        logoutButton = Button(self,text = "← Back",
                              command = lambda: desert.display_frame(Kinematics_Q_Start),
                              font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        logoutButton.grid(row = 0,column = 0)

        self.s, self.u, self.v, self.a, self.t, self.weight = 0,0,0,0,0,0

        Frame.config(self, bg = desert.BGColour)

        self.ansRightWrong = "" # Tell the user if they got the answers right or wrong

        self.visibleQ = "Please click the \"Generate Question\" button to generate a question to answer!" # Question shown is stored in this var
        self.ThirdVar = "" # 3rd variable given stored in this var
        self.GivenName = "" # Name of 3rd variable stored in this var
        
        self.answerNeeded1 = "" # First answer needed stored in this var
        self.answerNeeded2 = "" # Second answer needed stored in this var

        QGen = QHelper.Kinematics()

        topLabel = Label(self, text = "Kinematics Easy Weight Question Generator",font=desert.fontTitle,bg = desert.BGColour, fg = desert.TextColour)
        topLabel.grid(row = 1, column = 1, columnspan = 2)

        self.explanationLabel = Label(self, text = self.visibleQ,
                                      font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        self.explanationLabel.grid(column = 1, row = 2, columnspan = 2)

        self.ansRightWrongLabel = Label(self, text = self.ansRightWrong,
                                        font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        self.ansRightWrongLabel.grid(column = 3, row = 2)

        weightLabel1 = Label(self, text = "Weight:",
                             font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        weightLabel1.grid(row = 3, column = 1)

        self.weightLabel2 = Label(self, text = self.weight,
                                  font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        self.weightLabel2.grid(row = 3, column = 2)

        initalVLabel1 = Label(self, text = "Intial Velocity",
                              font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        initalVLabel1.grid(row = 4, column = 1)

        initalVLabel2 = Label(self, text = "0", font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        initalVLabel2.grid(row = 4, column = 2)

        self.ThirdVarLabel1 = Label(self, text = self.GivenName,
                                    font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour) # GivenName is going to be what it should show up as on the GUI - For example, "Time Taken" or "Distance Fallen"
        self.ThirdVarLabel1.grid(row = 5, column = 1)

        self.ThirdVarLabel2 = Label(self, text = self.ThirdVar,
                                    font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour) # ThirdVar is the actual value of the third variable given to them for the 5 variable equation - so 15.6, 10.4, etc.
        self.ThirdVarLabel2.grid(row = 5, column = 2)

        self.answerNeededLabel1 = Label(self, text = self.answerNeeded1,
                                        font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        self.answerNeededLabel1.grid(row = 6, column = 1)

        self.answerNeededEntry1 = Entry(self,width = 11,
                                        font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        self.answerNeededEntry1.grid(row = 6, column = 2)

        self.answerNeededLabel2 = Label(self, text = self.answerNeeded2,
                                        font = desert.fontBody, bg = desert.BGColour, fg = desert.TextColour)
        self.answerNeededLabel2.grid(row = 7, column = 1)

        self.answerNeededEntry2 = Entry(self, width = 11,
                                        font = desert.fontBody, bg = desert.ButtonColour, fg = desert.TextColour)
        self.answerNeededEntry2.grid(row = 7, column = 2)

        ansQButton = Button(self, text = "Submit!",
                            command = lambda: self.CheckAns(),
                            font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        ansQButton.grid(row = 98, column = 1, columnspan = 2)

        genQButton = Button(self, text = "Generate Question!",
                            command = lambda: self.showQ(QGen),
                            font = desert.fontButton, bg = desert.ButtonColour, fg = desert.TextColour, activebackground = desert.ButtonColour)
        genQButton.grid(row = 99, column = 1, columnspan = 2)

    def showQ(self,QGen):
        
        self.ansRightWrongLabel.config(text="")

        self.s, self.u, self.v, self.a, self.t, self.weight, s_or_v_or_t = QGen.simple_weight_q()

        self.visibleQ = "A ball is dropped. The ball has a weight of "+str(self.weight)+"kg and has an initial velocity of "+str(self.u)+"m/s."

        self.weightLabel2.config(text=self.weight)

        if s_or_v_or_t == 0: # If q is generated to give time...
            self.visibleQ = self.visibleQ + "\nThe ball is in the air for "+str(self.t)+" seconds. \nFind how far the ball falls in metres, \nand how fast it's final velocity is in m/s."
            self.GivenName = "Time Taken"
            self.ThirdVar = self.t
            self.answerNeeded1 = "Distance Fallen"
            self.answerNeeded2 = "Final Velocity"
        elif s_or_v_or_t == 1: # if q is generated to give distance...
            self.visibleQ = self.visibleQ + "\nThe ball falls "+str(self.s)+" metres before hitting the ground. \nFind out the final velocity of the ball in m/s, \nand the time it takes to hit the ground, in seconds."
            self.GivenName = "Distance Fallen"
            self.ThirdVar = self.s
            self.answerNeeded1 = "Final Velocity"
            self.answerNeeded2 = "Time Taken"
        elif s_or_v_or_t == 2: # if q is generated to give final velocity...
            self.visibleQ = self.visibleQ + "\nThe ball hits the ground with a final velocity of "+str(self.v)+"m/s. \nFind out the time taken by the ball to reach the ground in seconds, \nand the distance travelled to do so, in metres."
            self.GivenName = "Final Velocity"
            self.ThirdVar = self.v
            self.answerNeeded1 = "Time Taken"
            self.answerNeeded2 = "Distance Fallen"

        self.ThirdVarLabel1.config(text=self.GivenName)
        self.ThirdVarLabel2.config(text=self.ThirdVar)
        self.answerNeededLabel1.config(text=self.answerNeeded1)
        self.answerNeededLabel2.config(text=self.answerNeeded2)
        self.explanationLabel.config(text=self.visibleQ)

    def CheckAns(self):

        InputAns1 = self.answerNeededEntry1.get()
        if InputAns1 == "": #Error handling - stops it from trying to convert a string to a float.
            InputAns1 = 0

        InputAns2 = self.answerNeededEntry2.get()
        if InputAns2 == "": #Error handling - stops it from trying to convert a string to a float.
            InputAns2 = 0

        print("current values:", self.s, self.u, self.v, self.a, self.t, self.weight)

        if self.answerNeeded1 == "Distance Fallen" and self.answerNeeded2 == "Final Velocity":
            if float(InputAns1) == round(self.s,2):
                self.ansRightWrong = "First Answer Correct!"
            else:
                self.ansRightWrong = "First Answer Incorrect :("
                
            if float(InputAns2) == round(self.v,2):
                self.ansRightWrong += "\nSecond Answer Correct!"
            else:
                self.ansRightWrong += "\nSecond Answer Incorrect :("

            if float(InputAns1) == round(self.s,2) and float(InputAns2) == round(self.v,2):
                self.ansRightWrong = "Both Answers correct!"
                self.answerNeededEntry1.delete(0, "end")
                self.answerNeededEntry2.delete(0, "end")

        elif self.answerNeeded1 == "Final Velocity" and self.answerNeeded2 == "Time Taken":
            if float(InputAns1) == round(self.v,2):
                self.ansRightWrong = "First Answer Correct!"
            else:
                self.ansRightWrong = "First Answer Incorrect :("
                
            if float(InputAns2) == round(self.t,2):
                self.ansRightWrong += "\nSecond Answer Correct!"
            else:
                self.ansRightWrong += "\nSecond Answer Incorrect :("

            if float(InputAns1) == round(self.v,2) and float(InputAns2) == round(self.t,2):
                self.ansRightWrong = "Both Answers correct!"
                self.answerNeededEntry1.delete(0, "end")
                self.answerNeededEntry2.delete(0, "end")

        elif self.answerNeeded1 == "Time Taken" and self.answerNeeded2 == "Distance Fallen":
            if float(InputAns1) == round(self.t,2):
                self.ansRightWrong = "First Answer Correct!"
            else:
                self.ansRightWrong = "First Answer Incorrect :("
                
            if float(InputAns2) == round(self.s,2):
                self.ansRightWrong += "\nSecond Answer Correct!"
            else:
                self.ansRightWrong += "\nSecond Answer Incorrect :("

            if float(InputAns1) == round(self.t,2) and float(InputAns2) == round(self.s,2):
                self.ansRightWrong = "Both Answers correct!"
                self.answerNeededEntry1.delete(0, "end")
                self.answerNeededEntry2.delete(0, "end")

        self.ansRightWrongLabel.config(text = self.ansRightWrong)

###############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ STUDENT TEST PAGES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###############################################################################################




        

        

if __name__ == "__main__":
    program = mainWindow(Tk)
    #program.update_idletasks() # DELETE THIS IF SOMETHING BREAKS THAT SHOULDN'T - FORCES ALL IDLE TASKS (READS THROUGH CLASSES) TO BE DONE BEFORE
    #program.after(1000,update)
    program.mainloop() #         WINDOW HITS MAIN LOOP
