from tkinter import *
import tkinter as tk
#from TakeTest import TakeTest"""
"""RefTestName = "Unknown"
RefModules = "CM1202"
ReftotalMark = "10"
RefUserAns = [1, 1, 1, 1, 1, 6, 7, 8, 9, 1]
RefCorrectAns = [1, 1, 1, 1, 1, 6, 7, 8, 9, 1]"""
#lblQues = []
#Ref
#ShowAnswer(newWindow, TestName, Modules, totalMark, self.AnsQues, CsvCorrAns, self.lblQues, self.Ques)

a = 0 #Rows pointer for GUI setup
class ShowAnswer(Frame):
	def __init__(self, master, RefTestName, RefModules, ReftotalMark,  RefUserAns, RefCorrectAns, ReflblQues, RefQues, RefAnseQues):
		Frame.__init__(self,master)
		self.grid()
		self.createWidgets()
		self.RefTestName = RefTestName
		self.RefModules = RefModules
		self.ReftotalMark = ReftotalMark
		self.RefUserAns = RefUserAns
		self.RefCorrectAns = RefCorrectAns
		self.ReflblQues = ReflblQues
		self.RefQues = RefQues
		self.AnsQues = RefAnseQues

	def createWidgets(self):
		global a
		self.lblTestName = Label(self, text = self.RefTestName)
		self.grid(row = a, column = 0)

		self.lblTotalMark = Label(self, text = self.ReftotalMark)
		self.grid(row = a, column = 3)
		a += 1

		self.lblModules = Label(self, text = self.RefModules)
		self.grid(row = a, column = 0)

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


		for Ques in range(len(self.AnsQues)):
			#self.ReflblQues.append(Label(self, text = "Question" + str(Ques + 1) + ":"+self.CsvQues[Ques]))
			self.ReflblQues[Ques].grid(row = a, column = 0)
			
			self.UserAns.append(Label(self, text = self.RefUserAns[Ques]))
			self.UserAns[Ques].grid(row = a, column = 1)

			self.CorrectAns.append(Label(self, text = self.RefCorrectAns[Ques]))
			self.CorrectAns[Ques].grid(row = a, column = 2)

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