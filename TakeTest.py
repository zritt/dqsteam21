from tkinter import *
import tkinter as tk
import time
#from takeAssessment import moodle # Still not sure what valuable name
#from takeAssessment import userID # Still not sure what valuable name
#from assessment import typeOfAssessment # Still not sure what valuable name
#from assessment import timer #Still not sure what valuable name
#from assessment import lblDirt
import csv
#with open('assessments.csv', 'r') as csvfile:
	
	

typeOfAssessment = "formative"
moodle = ("1103")
timeleft = 5
b = 0

class TakeTest(Frame):
	#GUI Setup
	

	def __init__(self, master):
	#Initialise Questionnaire Class
		Frame.__init__(self,master)
		self.grid()
		# rows number for forming content
		self.lblMoodle = Label(self, text = "This is a " + typeOfAssessment + " test in moodle "+ moodle, font = ("MS", 16, "bold"))
		self.lblMoodle.grid(row = b, column = 0)
		
		self.lblTimer = Label(self, text = "Time:" +str(timeleft), font = ("MS", 14, "bold"))
		self.lblTimer.grid(row = b, column = 1)
		self.createWidgets()
		self.update_clock()
		
		
		#End _init_
#=================================End of copy================================================
	def createWidgets(self):
		a = b
		# Timer ref: https://stackoverflow.com/questions/25189554/countdown-clock-0105
		if typeOfAssessment == "Summative":
			# Space for starting timer created by tutor
			pass
		elif typeOfAssessment == "Formative":
			#Space for asking student to open optional timer
			pass

		a = a + 1
		lbl2ndLine = Label(self, text = "The first question start from below:", font = ("MS", 12, "bold") )
		lbl2ndLine.grid(row = a, column = 0)
		a = a + 1
		#print(lblDirt)
		c = 0 # Pointer for txtAns and radbtn
		self.lblQues = [] # Label list for Question
		self.Ques = [] # Empty Textbox list for Question
		self.radbtn = [] # Radio Button list on the form
		self.lblAns = [] # Textbox list for each answer on the form
		self.AnsQues = [None] * 10
		Question = "Question"

		#==================================================================================================================
		for Ques in range(len(self.AnsQues)):
			self.AnsQues[Ques] = IntVar()
			self.lblQues.append(Label(self, text = "Question" + str(Ques + 1) + ":"+Question))
			self.lblQues[Ques].grid(row = a, column = 0, sticky = W)
			
			a = a + 1   
			# Creating Labels and textboxs for each question		 
			for choose in range(0, 4, 2):
				self.radbtn.append(Radiobutton(self, variable = self.AnsQues[Ques], value = choose))
				self.radbtn[c].grid(row = a, column = 0, padx = 40, sticky = W)				
				#self.txtAns.append(Text(self, height = 0, width = 20))
				#self.txtAns[c].grid(row = a, column = 1, sticky = NW)
				self.lblAns.append(Label(self, text = "Answer: "+str(choose)))
				self.lblAns[c].grid(row = a, column = 0, padx = 60, sticky = W)

				self.radbtn.append(Radiobutton(self, variable = self.AnsQues[Ques], value = choose + 1))
				self.radbtn[c + 1].grid(row = a, column = 0, padx = 200, sticky = W)				
				#self.txtAns.append(Text(self, height = 0, width = 20))
				#self.txtAns[c].grid(row = a, column = 1, sticky = NW)
				self.lblAns.append(Label(self, text = "Answer: "+str(choose + 1)))
				self.lblAns[c + 1].grid(row = a, column = 0, padx = 220, sticky = W)

				a = a + 1
				c = c + 2
				# Creating radio buttons and textboxs for each choose in one question
		btnSubmit = Button(self, text = "Submit", font = ("MS", 16, "bold"))
		btnSubmit["command"] = self.storeResponse
		btnSubmit.grid(row = a, column = 1, sticky = W) 

		for ques in range(0, len(self.AnsQues)):
			self.AnsQues[ques].set(-1)
		#Empty all choose

	def storeResponse(self):
		#Store all content
		pass
		#End storeResponse()

	def update_clock(self):
		#Copy from https://stackoverflow.com/questions/2400262/how-to-create-a-timer-using-tkinter
		start = time.time()
		# time.time() returns the number of seconds since the unix epoch.
		# To find the time since the start of the function, we get the start
		# value, then subtract the start from all following values.
		time.clock()	
		# When you first call time.clock(), it just starts measuring
		# process time. There is no point assigning it to a variable, or
		# subtracting the first value of time.clock() from anything.
		# Read the documentation for more details.
		elapsed = 0
		while elapsed < timeleft:
			elapsed = time.time() - start
			out = timeleft - elapsed
			self.lblTimer.configure(text=("Time: " + str(out)))
			time.sleep(1) 
			






def Run():
#Run the program
	root = tk.Tk()
	app = TakeTest(root)
	root.mainloop()

Run() # Run the program
