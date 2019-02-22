from tkinter import *
from tkinter import messagebox
import assessment

class Question(Frame): # The (Frame) is needed to make sure this class is treated as a frame. 
	"""Widget to display questions"""
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()


		# Added this temporaily so I can check if you can boot the assessment from here.
		self.tutorLogin()
	
	def main(self):
		# main class to invoke other classes and display the window and GUI
		pass
		
	def createButton(self):
		# create buttons 
		btnStudent = Button(self, text = "Student login", font = ('Times', 8 , "bold"))
		btnStudent['command']= self.studentLogin
		btnStudent.grid(row = 5, column = 1 , columnspan = 2 )
		
		btnTutor = Button(self, text = "Tutor login", font = ('Times', 8 , "bold"))
		btnTutor['command'] = self.tutorLogin
		btnTutor.grid(row = 5, column = 3 , columnspan = 2 )
		
	def tutorLogin(self):
		lblProg = Label (self, text = 'Create assesment: ', font = ('Times', 10 , "bold"))
		lblProg.grid(row=0, column = 0 , columnspan =2 ,sticky= NE)
		
		btnSummative = Button ( self, text = "Create Summative assesment", font =('Times', 8 , "bold"))
		btnSummative['command'] = lambda: self.assessmentCreation('Summative')
		btnSummative.grid ( row = 2 , column = 1 , columnspan = 2)
		
		btnFormative = Button (self, text = "Create Formative assesment", font = ('Times', 8 , "bold"))
		btnFormative['command'] = lambda: self.assessmentCreation('Formative')
		btnFormative.grid(row = 2, column = 3 , columnspan = 2)

	def assessmentCreation(self, assessmentType):
		assessment = assessment.Assessment(Toplevel(self.master), assessmentType)
		
	def studentLogin(self):
		pass


	
# Main
if __name__ == '__main__':
	root = Tk()
	root.title("Login")
	app = Question(root)
	root.mainloop()