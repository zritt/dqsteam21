from tkinter import *
from user import *


class takeAssessment(Frame):
	#GUI Setup
	
	def __init__(self, master, inStudentId):
		Frame.__init__(self,master)
		self.grid()
		self.studentId = inStudentId
		self.createProgSelect()
		self.createStudentId(self.studentId)
		self.createButton()

	def createStudentId(self, inStudentId):
		lblProg = Label(self, text='Student ID: {}'.format(inStudentId), font=('sans-serif', 8,'bold'))
		lblProg.grid(row=0, column=0, columnspan=2, sticky=NE)

	def createProgSelect(self):
		lblProg = Label(self, text='Select the Assessment you want to take: ',
						font=('sans-serif', 8,'bold'))
		lblProg.grid(row=1, column=0, columnspan=2, sticky=NE)
		
		self.listProg = Listbox(self,height=3)
		scroll = Scrollbar(self,command = self.listProg.yview)
		self.listProg.configure(yscrollcommand=scroll.set)
		
		self.listProg.grid(row = 1, column =2 ,columnspan = 2 , sticky = NE)
		scroll.grid(row=1, column = 4, sticky = W)
		
		for item in ["module1", "module2", "module3"]:
			self.listProg.insert(END,item)
			
		self.listProg.selection_set(END) 
	
	def createButton(self):
		btnTakeTest= Button(self,text="Take Test")
		btnTakeTest.grid(row=5,column=2)
