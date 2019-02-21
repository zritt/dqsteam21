from tkinter import *
from tkinter import messagebox

class Question():
	"""Widget to display questions"""
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
	
	def main(self):
		# main class to invoke other classes and display the window and GUI
		
	def createButton(self):
		# create buttons 
		btnStudent = Button(self, text = "Student login", font = ('Times', 8 , "bold"))
		btnStudent['command']= self.studentLogin
		btnStudent.grid(row = 5, column = 1 , columnspan = 2 )
		
		btnTutor = Button(self, text = "Tutor login", font = ('Times', 8 , "bold"))
		btnTutor['command'] = self.tutorLogin
		btnTutor.grid(row = 5, column = 3 , columnspan = 2 )
		
	def tutorLogin(self):
		lblProg = Label (self, text = 'Create assesment: ', font = ('Times', 10 , "bold")
		lblProg.grid(row=0, column = 0 , columnspan =2 ,sticky= NE)
		
		btnSummative = Button ( self, text = "Create Summative assesment", font =('Times', 8 , "bold")
		btnSummative['command'] = self.SummativeAssesment
		btnSummative.grid ( row = 2 , column = 1 , columnspan = 2)
		
		btnFormative = Button (self, text = "Create Formative assesment", font = ('Times', 8 , "bold")
		btnFormative['command'] = self.FormativeAssesment
		btnFormative.grid(row = 2, column = 3 , columnspan = 2)
		
	def studentLogin(self):
		
		
		
	
	
	
	
	def tutorLogin(self):

	
# Main
if __name__ == '__main__':
	root = Tk()
	root.title("Login")
	app = Questionnaire(root)
	root.mainloop()