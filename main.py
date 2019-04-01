from tkinter import *
from user import *
from takeAssessment import *
from makeAssessment import *
from editAssessment import *
from report import *


class main(Frame):
	"""
	Main call will hold the main frame which will display all widgets and
	canvases. When initialised it inherit from its superclass Frame,
	and setting up the grid, it will then call LoginScreen method which will
	display the main login screen to the end user letting them choose
	between two options
	"""

	def __init__(self, master):
		Frame.__init__(self, master)  # inherit from Superclass Frame
		self.master = master  # master will be used to change titles of windows
		self.grid()  # setup the grid system to place widgets upon
		self.LoginScreen()  # start the program with student/ tutor login

	def LoginScreen(self):
		"""
		Main login screen which will display two options to the end user,
		student login and tutor login. Once pressed it will take them to
		their login screen respectively

		edit: removed create account option, seems redundant to add when
		testing will have inputted values within the csv files

		*The labels have been commented out but they are still operational*
		"""
		# window title screen
		self.master.title("Login")

		# resize window
		self.master.geometry("400x300")

		# Buttons specifying which option the end user can login with
		promptLbl = Label(self, text='Please select type of login: ',
						font=('sans-serif', 10,'bold'), justify="center")
		promptLbl.grid(row=0, column=0)

		btnStudent = Button(self, text="Student Login", command=self.studentLogin)
		btnStudent.grid(row=1, column=0, sticky=W, pady=10)

		btnTutor = Button(self, text="Tutor Login", command=self.tutorLogin)
		btnTutor.grid(row=1, column=1, padx=10, pady=10)

		# optional create account

		createAccountLbl = Label(self, text="I don't have an account: ", font=(
		'Arial', 10,'bold'))
		createAccountLbl.grid(row=2, column=0, sticky=W)

		btnNewAcc = Button(self, text="Create Account", command =
		self.createAccount)
		btnNewAcc.grid(row=3, column=0, sticky=W)

	def createAccount(self):
		self.master.title("Create an account")
		self.delete_children()

		createLbl = Label(self, text="Choose an option: ", font=(
			"sans-serif", 10, "bold"))
		createLbl.grid(row=0, column=0)

		studentAccountBtn = Button(self, text="Create Student",
								   command=self.createStudentPage)
		studentAccountBtn.grid(row=1, column=0, sticky=W)

		tutorAccountBtn = Button(self, text="Create Tutor",
								 command=self.createTutorPage)
		tutorAccountBtn.grid(row=1, column=1, padx=10)

	def createStudentPage(self):
		self.master.title("Create Student")
		self.delete_children()
		self.master.geometry("600x300")

		usernameLbl = Label(self, text="Enter your username: ", font=(
			"sans-serif", 8, "bold"))
		usernameLbl.grid(row=0, column=0, pady=5)

		self.usernameEntry = Entry(self)
		self.usernameEntry.grid(row=0, column=1, pady=5)

		fNameLbl = Label(self, text="Enter your first name: ", font=(
			"sans-serif", 8,"bold"))
		fNameLbl.grid(row=1, column=0, pady=5)

		self.fNameEntry = Entry(self)
		self.fNameEntry.grid(row=1, column=1, pady=5)

		lNameLbl = Label(self, text="Enter your last name: ", font=(
			"sans-serif", 8, "bold"))
		lNameLbl.grid(row=2, column=0, pady=5)

		self.lNameEntry = Entry(self)
		self.lNameEntry.grid(row=2, column=1, pady=5)

		passwordLbl = Label(self, text="Enter a password: ", font=(
			"sans-serif", 8, "bold"))
		passwordLbl.grid(row=3, column=0, pady=5)

		self.passwordEntry = Entry(self, show="*")
		self.passwordEntry.grid(row=3, column=1, pady=5)

		passwordReEnterLbl = Label(self, text="Re-Enter your password: ",
								   font=("sans-serif", 8, "bold"))
		passwordReEnterLbl.grid(row=4, column=0, pady=5)

		self.passwordReEnterEntry = Entry(self, show="*")
		self.passwordReEnterEntry.grid(row=4, column=1, pady=5)

		btnCreateAccount = Button(self, text="Create Account",
								  command=self.createStudent)
		btnCreateAccount.grid(row=5, column=1, pady=5)

	def createStudent(self):
		student = Student()

		username = self.usernameEntry.get()
		fName = self.fNameEntry.get()
		lName = self.lNameEntry.get()
		password = self.passwordEntry.get()
		checkPassword = self.passwordReEnterEntry.get()

		if password == checkPassword:
			if (username and fName and lName and password and checkPassword):
				studentNum = student.createNewStudent(username, fName, lName,
													  password)
				messagebox.showinfo("Account Creation Successful",
				"Your Account was successfully created and your student "
				"number is {}".format(studentNum))

				self.delete_children()
				self.LoginScreen()
			else:
				errorMsg = Label(self, text="One or more textboxes are "
											"empty, please fill them in!",
								 font=("sans-serif", 8, "bold"))
				errorMsg.grid(row=7, column=1)
		else:
			# display error msg
			errorMsg = Label(self, text="Passwords do not match!", font=(
				"sans-serif", 8, "bold"))
			errorMsg.grid(row=6, column=1)


	def createTutorPage(self):
		pass

	def studentLogin(self):
		"""
		Student login will ask the end user to enter their studentID and
		password, which will be checked against a csv file holding their
		credentials - handled in user class
		"""
		self.master.title("Student Login")  # change the title window
		# method which will remove all widgets from screen - refresh the window
		self.delete_children()

		studentIDLbl = Label(self, text="Enter Student's ID: ",
						font=('Arial', 8, 'bold'))
		studentIDLbl.grid(row=0, column=0, sticky=E, pady=5)

		# student Id textbox
		self.studentID = Entry(self)
		self.studentID.grid(row=0, column=1, columnspan=2, sticky=W, pady=5)

		passwordLbl = Label(self, text="Enter password: ",
						font=('Arial', 8, 'bold'))
		passwordLbl.grid(row=1, column=0, sticky=E, pady=5)

		# password textbox
		self.password = Entry(self, show="*")
		self.password.grid(row=1, column=1, columnspan=2, sticky=W, pady=5)

		btnLogin = Button(self,text="Login", command=self.checkStudentLogin)
		btnLogin.grid(row=2, column =1, sticky=W)

	def checkStudentLogin(self):
		"""
		Basic format checker to check if the student credentials are correct
		if so bring up the student menu which allows them to take assessments
		"""
		# initialise a student object, from user, to call its methods
		student = Student()
		# store the studentId entered in the form
		studentID = self.studentID.get()

		# check the student credentials
		if student.studentLogin(self.studentID.get(), self.password.get()):
			self.delete_frame_with_children()  # delete the current frame
			# display the assessment menu
			studentAssessment = takeAssessment(root, studentID)
		else:
			# display error message forcing the user to enter the credentials again
			ErrorMsg = Label(self, text="Login credentials are incorrect",
							 fg="red", font=("Verdana",8 ,"bold"))
			ErrorMsg.grid(row=3, column=1, sticky=W)

	def tutorLogin(self):
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
		tutorIDLbl.grid(row=0, column=0, sticky=E, pady=5)

		# tutor Id textbox
		self.tutorID = Entry(self)
		self.tutorID.grid(row=0, column=1, columnspan=2, sticky=W, pady=5)

		passwordLbl = Label(self, text="Enter password: ",
						font=('Arial', 8, 'bold'))
		passwordLbl.grid(row=1, column=0, sticky=E)

		# password textbox
		self.password = Entry(self, show="*")
		self.password.grid(row=1, column=1, columnspan=2, sticky=W, pady=5)

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
				"sans-serif", 10,"bold"))
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
		"""
		Will destroy every current widget within the frame, essentially
		allowing us to maintain a clean UI without everything remaining
		within the frame, saving resources
		"""
		for widget in Frame.winfo_children(self):
			widget.destroy()

	def delete_frame_with_children(self):
		"""
		Will make a call to delete_children, and then will go to forget the
		current frame, dropping it from resources then delete the current
		frame
		"""
		self.delete_children()
		Frame.grid_forget(self)
		Frame.destroy(self)


if __name__ == "__main__":
	# create a window
	root = Tk()

	# give each row and column a weight to essentially center it
	root.rowconfigure(0, weight=1)
	root.columnconfigure(0, weight=1)

	# call the main class to place a frame within the window made above
	app = main(root)

	# cause it to loop until exit or the 'X' is pressed
	root.mainloop()
