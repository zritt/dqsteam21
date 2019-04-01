from tkinter import *
from tkinter import messagebox
from user import *
from TakeTest import TakeTest
import csv


class takeAssessment(Frame):
	#GUI Setup
	
	def __init__(self, master, inStudentId):
		Frame.__init__(self,master)
		self.master = master
		self.master.geometry("600x400")
		self.grid()
		self.studentId = inStudentId
		self.createProgSelect()
		self.createStudentId(self.studentId)


	def createStudentId(self, inStudentId):
		studentIdLbl = Label(self, text='Student ID: {}'.format(inStudentId),
				  font=('sans-serif', 8,'bold'))
		studentIdLbl.grid(row=0, column=0, sticky=NE)

	def createProgSelect(self):
		formativeLbl = Label(self, text='Formative: ',
						font=('sans-serif', 8,'bold'))
		formativeLbl.grid(row=1, column=0, sticky=NE)

		formativeItems = self.readFormative()
		summativeItems = self.readSummative()


		self.stringVar1 = StringVar()
		self.stringVar1.set("Choose a Formative test to take by clicking it "
							"in the menu")

		self.dropdown1 = OptionMenu(self, self.stringVar1, *formativeItems,
								   command=self.doTest)

		self.dropdown1.grid(row=1, column=1)

		summativeLbl = Label(self, text="Summative: ",
							 font=("sans-serif", 8, "bold"))
		summativeLbl.grid(row=2, column=0)

		self.stringVar2 = StringVar()
		self.stringVar2.set("Choose a Summative test to take by clicking it "
							"in the menu")

		self.dropdown2 = OptionMenu(self, self.stringVar2, *summativeItems,
								   command=self.doTest)
		self.dropdown2.grid(row=2, column=1, pady=10)

	def doTest(self, value):
		newWindow = Toplevel()
		doTest = TakeTest(newWindow, self.studentId, value[1], 100)

	def readFormative(self):
		try:
			formativeLst = []
			with open('assessments.csv', 'r') as csvfile:
				csvreader = csv.reader(csvfile)
				csvLst = list(csvreader)
				for i in range(len(csvLst)):
					if csvLst[i][0] == "Formative":
						assessmentName = (csvLst[i - 2][0])
						moduleCode = (csvLst[i + 1][0])

						formativeLst.append((assessmentName, moduleCode))

			return formativeLst

		except FileNotFoundError:
			messagebox.showinfo("ERROR: Assessments.csv was not found")
			exit(1)

	def readSummative(self):
		try:
			summativeLst = []
			with open('assessments.csv', 'r') as csvfile:
				csvreader = csv.reader(csvfile)
				csvLst = list(csvreader)
				for i in range(len(csvLst)):
					if csvLst[i][0] == "Summative":
						assessmentName = (csvLst[i - 2][0])
						moduleCode = (csvLst[i + 1][0])

						summativeLst.append((assessmentName, moduleCode))

			return summativeLst

		except FileNotFoundError:
			messagebox.showinfo("ERROR: Assessments.csv was not found")
			exit(1)