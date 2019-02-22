from tkinter import *
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        #Form GUI
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        #End _init_    
    def createWidgets(self):
        lblFirstLine = Label(self, text = "Create test", font = ("MS", 12,"bold"))
        lblFirstLine.grid(row = 0, column = 0, rowspan = 3)
        #First Label End (row 0 - 2)#
        self.AnsQues = [None] * 10               
        a = 3 # rows number for forming content
        c = 0 # Pointer for txtAns and radbtn
        lblQues = [] # Label list for Question
        txtQues = [] # Empty Textbox list for Question
        radbtn = [] # Radio Button list on the form
        txtAns = [] # Textbox list for each answer on the form
        btnclear = [] # Button clear list on each question
#==================================================================================================================
        for Ques in range(5):
            self.AnsQues[Ques] = IntVar()
            lblQues.append(Label(self, text = "Question" + str(Ques + 1) + ":"))
            lblQues[Ques].grid(row = a, column = 0, padx = 10)
            txtQues.append(Text(self, height = 1,width = 40))
            txtQues[Ques].grid(row = a, column = 1)
            a = a + 1   
            # Creating Labels and textboxs for each question         
            for choose in range(4):
                radbtn.append(Radiobutton(self, variable = self.AnsQues[Ques], value = choose))
                radbtn[c].grid(row = a, column = 0, sticky=E)                
                txtAns.append(Text(self, height = 0, width = 20))
                txtAns[c].grid(row = a, column = 1, sticky = NW)
                a = a + 1
                c = c + 1
                # Creating radio buttons and textboxs for each choose in one question
            btnclear.append(Button(self, text = "Clear"))
            btnclear[Ques]["command"] = self.clearQues
            btnclear[Ques].grid(row = a - 1, column = 2)
            # Creating clear button for each question
        #End loop for creating every question with chooses
#===================================================================================================================
        btnSubmit = Button(self, text = "Submit")
        btnSubmit["command"] = self.storeResponse
        btnSubmit.grid(row = a, column = 1, sticky = W) 
        #Submit button
        btnClearAll = Button(self, text = "Clear All")
        btnClearAll["command"] = self.clearResponse
        btnClearAll.grid(row = a, column = 1, sticky = N)
        #ClearAll button
        #End createWidgets()
#===================================================================================================================

    def clearQues(self):
        #Clear everything in one of the question
        a = 1
        #End clearQues()

    def storeResponse(self):
        #Store all content
        a = 1
        #End storeResponse()

    def clearResponse(self):
        #Clear everything on the form
        a = 1
        #End clearResponse()

def Run():
	#Run the program
	root = tk.Tk()
	app = Application(root)
	root.mainloop()

Run() # Run the program