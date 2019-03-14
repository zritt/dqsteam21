from tkinter import *
import csv

class studentLogin(Frame):

	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.GUIstudent_login()
		self.button()
		
	def GUIstudent_login(self): 
		lblProg = Label(self, text="Enter Student's ID: ", font=('Arial', 8,'bold'))
		lblProg.grid(row=0, column=0, columnspan=1, sticky=NE)
		
		studentID = Text(self, height = 1, width = 15)
		studentID.grid(row = 0, column = 2, columnspan=2)
		
		lblProg = Label(self, text="Enter password: ", font=('Arial', 8,'bold'))
		lblProg.grid(row=2, column=0, columnspan=1, sticky=NE)
		
		password = Entry(self, show="*")
		password.grid(row = 2, column = 2, columnspan=2)
	def button(self):
		btnLogin = Button(self,text="Login")
		btnLogin.grid(row=3, column =2)

		
		
if __name__ == '__main__':
	root = Tk()
	root.title("Student Login")
	app = studentLogin(root)
	root.mainloop()