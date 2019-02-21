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
		btnStudent = Button(self)

	
# Main
root = Tk()
root.title("Login")
app = Questionnaire(root)
root.mainloop()