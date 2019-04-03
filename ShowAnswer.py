from tkinter import *
import tkinter as tk
import csv
#from TakeTest import TakeTest"""
TestName = "Unknown"
Modules = "CM1202"
totalMark = "10"
lblQues = []
CsvQues = []
CsvAns = []
CsvCorrAns = []

#Ref
#ShowAnswer(newWindow, TestName, Modules, totalMark, self.AnsQues, CsvCorrAns, self.lblQues, self.Ques)
def Readcsv():
		with open("assessments.csv", "r")as csvfile:
			csvreader = csv.reader(csvfile)
			l = list()
			global CsvQues
			global CsvAns
			global CsvCorrAns
			for row in csvreader:
				l.append(row) #Transfer reader into a list, just easier for me to maintain

			for i in range(len(l)): # for everything in the first column

				if l[i][0]==Modules and l[i-3][0] == TestName:# Find any matched Modules ID to identify which test

					for a in range(1, 11):# Take Questions from csv
						CsvQues.append(l[i-3][a])
						CsvCorrAns.append(l[i+2][a])
						for ChoColumn in range (1, 5):# Take Chooses from csv
							CsvAns.append(l[i-3+ChoColumn][a])
a = 0 #Rows pointer for GUI setup
class ShowAnswer(Frame):

	

	def __init__(self, master, RefTestName, RefModules, ReftotalMark,  RefUserAns, RefCorrectAns, ReflblQues, RefQues, RefAnseQues):
		Frame.__init__(self,master)
		#print("Name!:", RefTestName)
		"""self.RefTestName = RefTestName
		self.RefModules = RefModules
		self.ReftotalMark = ReftotalMark
		self.RefUserAns = RefUserAns
		self.RefCorrectAns = RefCorrectAns
		self.ReflblQues = ReflblQues
		self.RefQues = RefQues
		self.AnsQues = RefAnseQues"""
		global TestName
		global Modules
		global totalMark
		global UserAns
		global CorrectAns
		global lblQues
		global AnsQues
		TestName = RefTestName
		Modules = RefModules
		totalMark = ReftotalMark
		UserAns = RefUserAns
		CorrectAns = RefCorrectAns
		lblQues = ReflblQues
		Ques = RefQues
		AnsQues = RefAnseQues
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		Readcsv()
		global a
		print(TestName)
		self.lblTestName = Label(self, text = ("Test Name:", TestName))
		self.lblTestName.grid(row = a, column = 0)

		self.lblTotalMark = Label(self, text = ("Total Mark:", totalMark))
		self.lblTotalMark.grid(row = a, column = 3)
		a += 1

		self.lblModules = Label(self, text = ("Modules", Modules))
		self.lblModules.grid(row = a, column = 0)

		a +=1

		self.CorrectAns = []
		self.UserAns = []

		self.lblQuestion = Label(self, text = "Question:")
		self.lblQuestion.grid(row = a, column = 0)
		self.lblUserAnswers = Label(self, text = "Your Answers:")
		self.lblUserAnswers.grid(row = a, column = 1)
		self.lblCorrectAnswers = Label(self, text = "Correct Answers:")
		self.lblCorrectAnswers.grid(row = a, column = 2)

		a += 1
		self.Questions = []
		self.UserAnswers = []
		self.CorrectAnswers = []

		for Ques in range(len(AnsQues)):
			print("Number: ", Ques)
			#self.lblQuestion.append(Label(self, text = str(lblQues[Ques])))
			#lblQues[Ques].grid(row = a, column = 0)
			self.Questions.append(Label(self, text = CsvQues[Ques]))
			self.Questions[Ques].grid(row = a, column = 0)
			
			self.UserAnswers.append(Label(self, text = CsvAns[UserAns[Ques].get()]))
			self.UserAnswers[Ques].grid(row = a, column = 1)

			self.CorrectAnswers.append(Label(self, text = CsvAns[int(CorrectAns[Ques]) - 1]))
			self.CorrectAnswers[Ques].grid(row = a, column = 2)

			a += 1

		btnSubmit = Button(self, text = "Close", font = ("MS", 16, "bold"))
		btnSubmit["command"] = self.close
		btnSubmit.grid(row = a, column = 3)

	def close(self):
		self.master.destroy()

"""
def Run():
#Run the program
	root = tk.Tk()
	app = ShowAnswer(root)
	root.mainloop()

Run() # Run the program

"""