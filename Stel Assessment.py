
38 lines (27 sloc) 1000 Bytes
from tkinter import *
#mport tkinter as Tk

class Assessment(Frame):
	#GUI Setup
	
	def __init__(self, master):
	#Initialise Questionnaire Class
		Frame.__init__(self,master)
		self.grid()
		self.ChooseAssessment()
		
	def ChooseAssessment(self):
		
		lblProg = Label(self, text='Choose Assessment: ', font=('MS', 8,'bold'))
		lblProg.grid(row=0, column=0, columnspan=2, sticky=NE)
		
		lblProg = Label(self, text='Formative Assessment ', font=('MS', 8,'bold'))
		lblProg.grid(row=1, column=0, columnspan=2, sticky=NE)
		self.varQ1 = IntVar()
		R1Q1 = Radiobutton(self, variable=self.varQ1, value=1)
		R1Q1.grid(row=1, column= 3)
		
		lblProg = Label(self, text='Summative Assessment ', font=('MS', 8,'bold'))
		lblProg.grid(row=1, column=4, columnspan=2, sticky=NE)
		R1Q2 = Radiobutton(self, variable=self.varQ1, value=2)
		R1Q2.grid(row=1, column= 6)
	#def AddQuestion(self):
		

if __name__ == '__main__':
	root = Tk()
	root.title("System Login")
	app = Assessment(root)
root.mainloop()