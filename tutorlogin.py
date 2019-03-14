from tkinter import *
import csv

class tutorLogin(Frame):

	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.GUItutor_login()
		self.button()
		
	def GUItutor_login(self): 
		lblProg = Label(self, text="Enter Tutor's ID: ", font=('Arial', 8,'bold'))
		lblProg.grid(row=0, column=0, columnspan=1, sticky=NE)
		
		tutorID = Text(self, height = 1, width = 15)
		tutorID.grid(row = 0, column = 2, columnspan=2)
		
		lblProg = Label(self, text="Enter password: ", font=('Arial', 8,'bold'))
		lblProg.grid(row=2, column=0, columnspan=1, sticky=NE)
		
		password = Entry(self, show="*")
		password.grid(row = 2, column = 2, columnspan=2)
	
	def button(self):
		btnLogin = Button(self,text="Login")
		btnLogin.grid(row=7, column =2)

		
		
if __name__ == '__main__':
	root = Tk()
	root.title("Student Login")
	app = tutorLogin(root)
	root.mainloop()