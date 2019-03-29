from tkinter import *

class tutorLogin(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)

	def Tutor_Login(self):
		"""
		Tutor login will ask the end user to login using their TutorId and
		password, which will be checked against a csv file holding their
		credentials - handled in user class
		"""
		self.master.title("Tutor Login")  # change the window title
		# refresh the current the frame
		self.delete_children()

		tutorIDLbl = Label(self, text="Enter Tutor ID: ",
						font=('Arial', 8, 'bold'))
		tutorIDLbl.grid(row=0, column=0, sticky=E)

		# tutor Id textbox
		self.tutorID = Entry(self)
		self.tutorID.grid(row=0, column=1, columnspan=2, sticky=W)

		passwordLbl = Label(self, text="Enter password: ",
						font=('Arial', 8, 'bold'))
		passwordLbl.grid(row=1, column=0, sticky=E)

		# password textbox
		self.password = Entry(self, show="*")
		self.password.grid(row=1, column=1, columnspan=2, sticky=W)

		btnLogin = Button(self,text="Login", command=self.checkTutorLogin)
		btnLogin.grid(row=2, column =1, sticky=W)

	def checkTutorLogin(self):
		"""
		Basic format checker to check the Tutor credentials against a csv
		file, if correct display the tutor menu allowing them make
		assessments, edit assessments and view reports
		"""
		# initialise a tutor object, from user, to call its methods
		tutor = Tutor()
		# store the tutorID value from the form
		self.tutorIDString = self.tutorID.get()

		# check the tutor credentials
		if tutor.tutorLogin(self.tutorIDString, self.password.get()):
			self.delete_children()  # refresh the frame

			instrLbl = Label(self, text="Please choose an option:", font=(
				"sans-serif", 8,"bold"))
			instrLbl.grid(row=0, column=0, columnspan=1)

			# each button will call a command to do what the button says
			createAssessementBtn = Button(self, text="Create an Assessment",
										  command=self.createAssessment)
			createAssessementBtn.grid(row=1, column=0, padx=10, pady=10)

			editAssessmenmtBtn = Button(self, text="Edit an Assessment",
										command=self.editAssessment)
			editAssessmenmtBtn.grid(row=1, column=1, padx=10, pady=10)

			reportBtn = Button(self, text="View Reports",
							   command=self.viewReports)
			reportBtn.grid(row=1, column=3, padx=10, pady=10)
		else:
			# display an error message, causing the user to use the correct credentials
			ErrorMsg = Label(self, text="Login credentials are incorrect", fg="red", font=("Verdana",8 ,"bold"))
			ErrorMsg.grid(row=3, column=1, sticky=W)

	def createAssessment(self):
		"""
		From the tutor menu, will call the ChooseAssessmentType class from the
		makeAssessment script, allowing the tutor to create an assessment of
		two types, 'formative' and 'summative'. This will be made in a
		separate window allowing the tutor to choose from the other two
		options if they wish, or create even more assessments
		"""
		# create a child window
		newWindow = Toplevel(root)
		# place the assessment creation wizard in the child window
		tutorAssessment = ChooseAssessmentType(newWindow, self.tutorIDString)

	def editAssessment(self):
		"""
		From the tutor menu, will call ChooseAssessment class from
		editAssessment script, allowing the tutor to edit the assessments
		they have created from a dropdown menu. This will be made in a
		separate window allowing the tutor to choose from the other two
		options if they wish, or edit even more assessments.
		"""
		# create a child window
		newWindow = Toplevel(root)
		# place the edit assessment wizard in the child window
		tutorAssessment = ChooseAssessment(newWindow)

	def viewReports(self):
		"""
		From the tutor menu, will call Report class from the report script,
		allowing the tutor to view assessment results with the following
		table column headers: StudentID, Firstname, Lastname, Testname and
		score.  This will be made in a separate window allowing the tutor to
		choose from the other two options if they wish, or view the reports
		again
		"""
		# crete a chole window
		newWidow = Toplevel(root)
		# place the report table in the child window
		reports = Report(newWidow)