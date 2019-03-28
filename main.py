from tkinter import *
import csv
from user import Student, Tutor
from takeAssessment import *
from makeAssessment import *
from studentLogin import *

#from Response import Response
#import tkMessageBox

class main(Frame):
	#GUI Setup
	
	def __init__(self, master):
	#Initialise Questionnaire Class
		Frame.__init__(self,master)
		self.grid()
		self.LoginScreen()
		
	def LoginScreen(self):
		lblProg = Label(self, text='Please select type of login: ', font=('Arial', 8,'bold'))
		lblProg.grid(row=0, column=0, columnspan=1, sticky=NE)
	
		btnStudent = Button(self,text="Student Login",command = self.Student_Login)
		btnStudent.grid(row=3,column=0)
		
		btnTutor = Button(self,text="Tutor Login", command = self.Tutor_Login)
		btnTutor.grid(row=3,column=1)
		
		lblProg = Label(self, text="I don't have an account: ", font=('Arial', 8,'bold'))
		lblProg.grid(row=4, column=0, columnspan=1, sticky=NE)
		
		btnNewAcc = Button ( self, text="Create Account", command = self.Create_Account)
		btnNewAcc.grid(row=5,column =0)
		


	def Student_Login(self):
		StudentNumber = input(str("Enter Student Number: "))
		StudentPass = input("Enter Password: ")
		student = Student()
		if student.studentLogin(StudentNumber, StudentPass):
			studentAssessment = takeAssessment(root, StudentNumber)
			
		
		
		
		
		
	def Tutor_Login(self):
		TutorNumber = input(str("Enter Tutor Number: " ))
		TutorPass = input("Enter Password: ")
		tutor = Tutor()
		if tutor.tutorLogin(TutorNumber, TutorPass):
			tutorAssessment = ChooseAssessment(root, tutor.tutorNumber)
		
		
	
	def Create_Account(self):
		user = input(str("Are you a student or a tutor?  "))
		while user != "tutor" and user != "student":
			user = input(str("Are you a student or a tutor?"))
		if user == "tutor":
			NewTutorName = input(str("Enter your Name: "))
			NewTutorSurname = input(str("Enter your Surname: "))
			NewTutorEmail = input("Enter your email: ")
			NewTutorPass = input("Enter a password: ")
			confirmPass = input("Re-enter your password: " )
			while confirmPass != NewTutorPass:
				confirmPass = input("Re-enter your password: " )
			print("success")
		else:
			NewStudentName = input(str("Enter your Name: "))
			NewStudentSurname = input(str("Enter your Surname: "))
			NewStudentEmail = input("Enter your Email: ")
			NewStudentPass = input("Enter a password: ")
			confirmPassS = input("Re-enter your password: ")
			while confirmPassS != NewStudentPass:
				confirmPass = input("Re-enter your password: " )
			print("success")
	
	

#Main
if __name__ == '__main__':
	root = Tk()
	root.title("System Login")
	app = main(root)
	root.mainloop()