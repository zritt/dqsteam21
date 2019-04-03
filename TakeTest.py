from tkinter import *
import tkinter as tk
import time
import csv
from ShowAnswer import ShowAnswer
#def __init__(self, master, RefStuID, RefModules, RefTime, RefTestName):
typeOfAssessment = "Unknown"
Modules = ("CM1210")
timeleft = 100
b = 0 #Rows pointer in GUI setting up
StudentID = "1"
TestName = "TestSummativeEdited"
FirstName = "Unknown"
LastName = "Unknown"

CsvCorrAns = []

def ReadStudentName():
	#Use studentID as key to search student's name
	global FirstName
	global LastName
	with open("students.csv", "r")as csvfile:
		csvreader = csv.reader(csvfile)
		for rows in csvreader:		
			if rows[0] == StudentID:
				FirstName = str(rows[3])
				LastName = str(rows[4])
				break
def Show(self, totalMark):
	global CsvQues

	newWindow = Toplevel()
	show = ShowAnswer(newWindow, TestName, Modules, totalMark, self.AnsQues,CsvCorrAns, self.lblQues, self.Ques, self.AnsQues)
	self.master.destroy()

class TakeTest(Frame):
	#GUI Setup

	#def _init(self, master):
	#def __init__(self, master, RefStuID, RefModules, RefTime, RefTestName):
	def __init__(self, master, RefStuID, RefModules, RefTime, RefTestName):
	#Initialise Questionnaire Class
		global timeleft
		global StudentID
		global Modules
		global TestName

		TestName = RefTestName
		timeleft = RefTime
		StudentID = RefStuID
		Modules = RefModules
		ReadStudentName()
		Frame.__init__(self,master)

		self.grid()
		# rows number for forming content
		self.lblModules = Label(self, text = "This is a " + typeOfAssessment + " test in Modules "+ Modules, font = ("MS", 16, "bold"))
		self.lblModules.grid(row = b, column = 0)
		self.lblTimer = Label(self, text = "", font = ("MS", 14, "bold"))
		self.lblTimer.grid(row = b, column = 1)
		self.timeleft = timeleft
		self.createWidgets()
		
		
		#End _init_
#=================================End of copy================================================
	def createWidgets(self):

		global CsvQues

		a = b
		a = a + 1
		lbl2ndLine = Label(self, text = "The first question start from below:", font = ("MS", 12, "bold") )
		lbl2ndLine.grid(row = a, column = 0)
		a = a + 1
		#print(lblDirt)
		c = 0 # Pointer for txtAns and radbtn
		d = 0 # Pointer for each questions to display chooses
		self.lblQues = [] # Label list for Question
		self.Ques = [] # Empty Textbox list for Question
		self.radbtn = [] # Radio Button list on the form
		self.lblAns = [] # Textbox list for each answer on the form
		self.AnsQues = [None] * 10
		Question = "Question"
		with open("assessments.csv", "r")as csvfile:
			csvreader = csv.reader(csvfile)
			l = list()
			CsvQues = []
			CsvAns = []
			for row in csvreader:
				l.append(row) #Transfer reader into a list, just easier for me to maintain

			for i in range(len(l)): # for everything in the first column

				if l[i][0]==Modules and l[i-3][0] == TestName:# Find any matched Modules ID to identify which test
					global typeOfAssessment
					if l[i-1][0] == "Summative":
						self.update_clock(timeleft)
						
					for a in range(1, 11):# Take Questions from csv
						CsvQues.append(l[i-3][a])
						CsvCorrAns.append(l[i+2][a])
						for ChoColumn in range (1, 5):# Take Chooses from csv
							CsvAns.append(l[i-3+ChoColumn][a])

					self.lblModules.configure(text="This is a " + str(l[i-1][0]) + " test in Modules "+ str(l[i][0]))
					
		#==================================================================================================================
		for Ques in range(len(self.AnsQues)):
			self.AnsQues[Ques] = IntVar()
			self.lblQues.append(Label(self, text = "Question" + str(Ques +  1) + ":"+CsvQues[Ques]))
			self.lblQues[Ques].grid(row = a, column = 0, sticky = W)
			
			a = a + 1	
			# Creating Labels and textboxs for each question		 
			for choose in range(0, 4, 2):
				self.radbtn.append(Radiobutton(self, variable = self.AnsQues[Ques], value = choose))
				self.radbtn[c].grid(row = a, column = 0, padx = 40, sticky = W)				
				#self.txtAns.append(Text(self, height = 0, width = 20))
				#self.txtAns[c].grid(row = a, column = 1, sticky = NW)
				#self.lblAns.append(Label(self, text = "Answer: "+str(choose)))
				self.lblAns.append(Label(self, text = "Answer: "+CsvAns[d]))
				d = d + 1
				self.lblAns[c].grid(row = a, column = 0, padx = 60, sticky = W)


				self.radbtn.append(Radiobutton(self, variable = self.AnsQues[Ques], value = choose + 1))
				self.radbtn[c + 1].grid(row = a, column = 0, padx = 200, sticky = W)				
				#self.txtAns.append(Text(self, height = 0, width = 20))
				#self.txtAns[c].grid(row = a, column = 1, sticky = NW)
				self.lblAns.append(Label(self, text = "Answer: "+CsvAns[d]))
				d = d + 1
				self.lblAns[c + 1].grid(row = a, column = 0, padx = 220, sticky = W)

				a = a + 1
				c = c + 2
				# Creating radio buttons and textboxs for each choose in one question
		self.lblWarning = Label(self, text = "")
		self.lblWarning.grid(rows = a, column = 0)
		a = a + 1
		btnSubmit = Button(self, text = "Submit", font = ("MS", 16, "bold"))
		btnSubmit["command"] = self.storeResponse
		btnSubmit.grid(row = a, column = 1, sticky = W) 

		for ques in range(0, len(self.AnsQues)):
			self.AnsQues[ques].set(-1)
		#Empty all choose



	def storeResponse(self):
		#Store all content into results.csv
		#Format: 
		#===> StudentID, TestName, User's input [0:9], first Name, Last Name, Total Mark

		#Can only submit if no questions is empty
		#Window will close when submit.
		AllFill = False
		totalMark = 0
		for i in range(0, len(self.AnsQues)):
			if (self.AnsQues[i].get() == -1):
				AllFill = True
				
		if AllFill == True:
			self.lblWarning.configure(text=("One or more questions didnt answered"))
		else:
			rows = [StudentID, TestName]
			for i in range(0, len(self.AnsQues)):
				rows.append(str(self.AnsQues[i].get()))
				if (self.AnsQues[i].get() == int(CsvCorrAns[i]) - 1):
					totalMark = totalMark + 1
			rows.append(FirstName)
			rows.append(LastName)
			rows.append(totalMark)
			with open("results.csv", mode = 'a', newline='') as csv_file:
				ResultWriter = csv.writer(csv_file, delimiter = ",")
				row = []
				row.append(rows)
				ResultWriter.writerows(row)
			#self.master.destroy()
			Show(self, totalMark)



		#End storeResponse()
	
	def update_clock(self, remaining = None):
	# Copy from https://stackoverflow.com/questions/10596988/making-a-countdown-timer-with-python-and-tkinter
	# And added some function I needed
		Tempmin = 0
		Tempsecond = 0
		Temp = ""
				
		if remaining is not None:
			self.remaining = remaining

		if self.remaining >=60:
			Tempmin = int(self.remaining / 60)
			Tempsecond = self.remaining % 60
			Temp = str(f"{Tempmin:02d}")+":"+str(f"{Tempsecond:02d}")
		else:
			Temp = "00:"+str(f"{self.remaining:02d}")

		if self.remaining <= 0:
			self.lblTimer.configure(text="time's up!")
		else:
			self.lblTimer.configure(text=Temp)
			self.remaining = self.remaining - 1
			self.after(1000, self.update_clock)


""""
def Run():
#Run the program
	root = tk.Tk()
	app = TakeTest(root)
	root.mainloop()

Run() # Run the program
"""
