from tkinter import *
import csv
from user import *
from takeAssessment import *
from makeAssessment import *
from editAssessment import *


class main(Frame):
	#GUI Setup

	def __init__(self, master):
		Frame.__init__(self,master)
		self.master = master
		self.grid()
		self.LoginScreen()

	def LoginScreen(self):

		self.master.title("Login")

		lblProg = Label(self, text='Please select type of login: ',font=('Arial', 8,'bold'), justify="center")
		lblProg.grid(row=0, column=0, sticky=NE)

		btnStudent = Button(self,text="Student Login",command =self.Student_Login)
		btnStudent.grid(row=1,column=0, columnspan=1 ,sticky=W)

		btnTutor = Button(self,text="Tutor Login", command = self.Tutor_Login)
		btnTutor.grid(row=1,column=1, sticky=E)

		#lblProg = Label(self, text="I don't have an account: ", font=(
		# 'Arial', 8,'bold'))
		#lblProg.grid(row=4, column=0, columnspan=1, sticky=NE)

		#btnNewAcc = Button ( self, text="Create Account", command =
		# self.Create_Account)
		#btnNewAcc.grid(row=5,column =0)



	def Student_Login(self):
		self.master.title("Student Login")
		self.delete_children()

		lblProg = Label(self, text="Enter Student's ID: ",
						font=('Arial', 8, 'bold'))
		lblProg.grid(row=0, column=0, sticky=E)

		self.studentID = Entry(self)
		self.studentID.grid(row=0, column=1, columnspan=2, sticky=W)

		lblProg = Label(self, text="Enter password: ",
						font=('Arial', 8, 'bold'))
		lblProg.grid(row=1, column=0, sticky=E)

		self.password = Entry(self, show="*")
		self.password.grid(row=1, column=1, columnspan=2, sticky=W)

		btnLogin = Button(self,text="Login", command=self.checkStudentLogin)
		btnLogin.grid(row=2, column =1, sticky=W)

		placeholderLbl = Label(self)
		placeholderLbl.grid(row=3, column=1, sticky=W)


	def checkStudentLogin(self):
		student = Student()
		studentID = self.studentID.get()
		if student.studentLogin(self.studentID.get(), self.password.get()):
			self.delete_frame_with_children()
			studentAssessment = takeAssessment(root, studentID)
		else:
			ErrorMsg = Label(self, text="Login credentials are incorrect",
							 fg="red", font=("Verdana 8 bold"))
			ErrorMsg.grid(row=3, column=1, sticky=W)


	def Tutor_Login(self):
		self.master.title("Tutor Login")
		self.delete_children()

		lblProg = Label(self, text="Enter Tutor ID: ",
						font=('Arial', 8, 'bold'))
		lblProg.grid(row=0, column=0, sticky=E)

		self.tutorID = Entry(self)
		self.tutorID.grid(row=0, column=1, columnspan=2, sticky=W)

		lblProg = Label(self, text="Enter password: ",
						font=('Arial', 8, 'bold'))
		lblProg.grid(row=1, column=0, sticky=E)

		self.password = Entry(self, show="*")
		self.password.grid(row=1, column=1, columnspan=2, sticky=W)

		btnLogin = Button(self,text="Login", command=self.checkTutorLogin)
		btnLogin.grid(row=2, column =1, sticky=W)

		placeholderLbl = Label(self)
		placeholderLbl.grid(row=3, column=1, sticky=W)

	def checkTutorLogin(self):
		tutor = Tutor()
		self.tutorIDString = self.tutorID.get()
		if tutor.tutorLogin(self.tutorIDString, self.password.get()):
			self.delete_children()

			createAssessementBtn = Button(self, text="Create an Assessment",
										  command=self.createAssessment)
			createAssessementBtn.grid(row=0, column=0, sticky=W)

			editAssessmenmtBtn = Button(self, text="Edit an Assessment",
										command=self.editAssessment)
			editAssessmenmtBtn.grid(row=0, column=1, sticky=E)
		else:
			ErrorMsg = Label(self, text="Login credentials are incorrect", fg="red", font=("Verdana 8 bold"))
			ErrorMsg.grid(row=3, column=1, sticky=W)

	def createAssessment(self):
		newWindow = Toplevel(root)
		tutorAssessment = ChooseAssessmentType(newWindow, self.tutorIDString)


	def editAssessment(self):
		newWindow = Toplevel(root)
		tutorAssessment = ChooseAssessment(newWindow)

	"""
	def Create_Account(self):
		user = input(str("Are you a student or a tutor?  "))
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
	"""

	def delete_children(self):
		for widget in Frame.winfo_children(self):
			widget.destroy()

	def delete_frame_with_children(self):
		self.delete_children()
		Frame.grid_forget(self)
		Frame.destroy(self)


if __name__ == "__main__":
	root = Tk()
	root.geometry("400x100")
	root.rowconfigure(0, weight=1)
	root.columnconfigure(0, weight=1)
	app = main(root)
	root.mainloop()
