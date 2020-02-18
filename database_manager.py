import sqlite3 as sql
import security as security

class DatabaseManipulate:

    def __init__(self):
        self.mech_db = sql.connect("database/mechanics_database.db")
        self.b = self.mech_db.cursor()

        self.b.execute("""PRAGMA foreign_keys = ON;""") # Enables foreign keys since they're disabled by default
        
        self.mech_db.commit()

    def startup(self):

        # Order of generation might seem odd - it's to ensure that a table exists before the program
        # tries to make a foreign key and reference a non-existant table. 
        
        # Make Teacher table (Admin users)
        self.b.execute("""CREATE table if not exists Teachers
                  (Teacher_ID text,
                  Teacher_Title text,
                  Teacher_LastName text,
                  Teacher_Password text,
                  PRIMARY KEY("Teacher_ID"))
                  """)

        # Make Test Table
        self.b.execute("""CREATE table if not exists Tests
                  (Test_ID text,
                  Test_Name text,
                  Test_MaxMark text,
                  PRIMARY KEY("Test_ID"))
                  """)

        # make class table
        self.b.execute("""CREATE table if not exists Class
                  (Class_ID text,
                  Teacher_ID text,
                  Test_ID text,
                  PRIMARY KEY("Class_ID"),
                  FOREIGN KEY(Teacher_ID) REFERENCES Teachers(Teacher_ID),
                  FOREIGN KEY(Test_ID) REFERENCES Tests(Test_ID))
                  """)
        
        # Make students table
        self.b.execute("""CREATE table if not exists Students
                  (Student_ID text,
                  Student_FirstName text,
                  Student_LastName text,
                  Class_ID text,
                  Student_Password text,
                  PRIMARY KEY("Student_ID"),
                  FOREIGN KEY(Class_ID) REFERENCES Class(Class_ID))
                  """)
        
        # Make classTest linking table
        self.b.execute("""CREATE table if not exists ClassTest
                  (StudentTest_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  Test_ID text,
                  Student_ID text,
                  Student_Score number,
                  Student_Comment text,
                  FOREIGN KEY(Test_ID) REFERENCES Tests(Test_ID),
                  FOREIGN KEY(Student_ID) REFERENCES Students(Student_ID))
                  """)
        
        # Make Questions table
        self.b.execute("""CREATE table if not exists Questions
                  (Quest_ID text,
                  Question_Type text,
                  Question_Data text,
                  Question_Marks number,
                  Test_ID text,
                  PRIMARY KEY("Quest_ID"),
                  FOREIGN KEY(Test_ID) REFERENCES Tests(Test_ID))
                  """)

    def foreignKeys(self):
        self.b.execute("""UPDATE Students FOREIGN KEY(Class_ID) REFERENCES Class(Class_ID)""")
        self.b.execute("""""")
        self.mech_db.commit()

    def addStudent(self,ID,FirstName,LastName,Password,Class_ID):
        self.b.execute("""INSERT INTO Students VALUES(?,?,?,?,?);""",(ID,FirstName,LastName,Class_ID,Password))
        self.mech_db.commit()

    def addTeacher(self,ID,Title,LastName,Password):
        self.b.execute("""INSERT INTO Teachers VALUES(?,?,?,?);""",(ID,Title,LastName,Password))
        self.mech_db.commit()

    def addClass(self,ID,Teacher,TestID):
        self.b.execute("""INSERT INTO Class VALUES(?,?,?);""",(ID,Teacher,TestID))
        self.mech_db.commit()

    def addTest(self,ID,Name,MaxMark):
        self.b.execute("""INSERT INTO Tests VALUES(?,?,?);""",(ID,Name,MaxMark))
        self.mech_db.commit()

    def addQuestion(self,ID,Type,Data,Marks,TestID,Answer):
        self.b.execute("""INSERT INTO Questions VALUES (?,?,?,?,?,?);""",(ID,Type,Data,Marks,TestID,Answer))
        self.mech_db.commit()
        
    def addResults(self,Test_ID,Student_ID,Score,Comment):
        self.b.execute("""INSERT INTO ClassTest(Test_ID,Student_ID,Student_Score,Student_Comment) VALUES(?,?,?,?);""",(Test_ID,Student_ID,Score,Comment))
        self.mech_db.commit()

    def fixQuestion(self):
        self.b.execute("""ALTER TABLE Questions CHANGE QMark QAnswer number;""")
        self.mech_db.commit()
        
    def makeDefaults(self):

        studentPass = "passport"
        adminPass = "passw0rd"

        studentPass = security.genHash(studentPass)
        adminPass = security.genHash(adminPass)
        
        self.b.execute("""INSERT INTO Tests(Test_ID,Test_Name,Test_MaxMark)
                        VALUES("proj-1", "Projectiles 1", 12)""")

        self.b.execute("""INSERT INTO Teachers(Teacher_ID,Teacher_Title,Teacher_LastName,Teacher_Password) VALUES("admin", "Mr", "Jeffries", '{}')""".format(adminPass))
        
        self.b.execute("""INSERT INTO Class(Class_ID,Teacher_ID,Test_ID)
                       VALUES("12A", "admin", "proj-1")""")
        
        self.b.execute("""INSERT INTO Students(Student_ID,Student_FirstName,Student_LastName,Class_ID,Student_Password) VALUES("Student", "Default", "McStudentFace", "12A", '{}')""".format(studentPass))
        
        self.mech_db.commit() #Creates 2 default profiles inside of the database for testing

    def StudentLoginCheck(self,username,password):
        self.b.execute("""SELECT Student_ID, Student_Password FROM Students WHERE Student_ID = '{}'""".format(username))
        StudentData = self.b.fetchone() # Fetch the record with the given ID

        if StudentData == None: #If no record is found, create a tuple containing 2 falses to prevent errors
            StudentData = (False,False)

        return StudentData #Return the tuple for login verification


    def AdminLoginCheck(self,username,password):
        self.b.execute("""SELECT Teacher_ID, Teacher_Password FROM Teachers WHERE Teacher_ID = '{}'""".format(username))
        TeacherData = self.b.fetchone() # Fetch the record with the given ID/username

        if TeacherData == None: # If no record is found, create a tuple of 2 falses to prevent errors
            TeacherData = (False,False)

        return TeacherData # Return the tuple for login verification

    def allStudentData(self):
        self.b.execute("""SELECT * FROM Students""")
        AllStudentData = self.b.fetchall()

        return AllStudentData

    def allTableData(self,Table):
        self.b.execute("SELECT * FROM "+Table)
        AllData = self.b.fetchall()

        return AllData

    def delARecord(self, Data, Table, ID):
        self.b.execute("DELETE FROM "+Table+" WHERE "+ID+" = '"+Data["text"]+"'")
        self.mech_db.commit()

    def delOneStudent(self,stuData):
        self.b.execute("""DELETE FROM Students WHERE Student_ID = '{}'""".format(stuData["text"]))
        self.mech_db.commit()

        
    def CloseBase(self):
        self.mech_db.close() # Close the database - use sparingly! known to break a lot of things a lot of the time 
        

if __name__ == "__main__":
    jeffery = DatabaseManipulate()
    jeffery.fixQuestion()

    
