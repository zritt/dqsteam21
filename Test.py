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
        a = 0
        # rows number for forming content
        lblFirstLine = Label(self, text = "Create Assessment", font = ("MS", 12,"bold"))
        lblFirstLine.grid(row = a, column = 0)
        a = a + 1
        #First Label End#
        lblChoose = Label(self, text = 'Choose Assessment: ', font=('MS', 8,'bold'))
        lblChoose.grid(row = a, column = 0, sticky = W)
        a = a + 1
        # Label for telling It is Choose Assessment
        lblForAss = Label(self, text = 'Formative Assessment ', font = ('MS', 8,'bold'))
        lblForAss.grid(row = a, column = 1, sticky = W)
        # Label of Formative Assessment
        self.varTypeOfAss = IntVar()
        RForAss = Radiobutton(self, variable = self.varTypeOfAss, value = 1)
        RForAss.grid(row = a, column = 1, sticky = NE)
        a = a + 1
        # RadioButton for choosing Formative Assessment
        lblSumAss = Label(self, text='Summative Assessment ', font = ('MS', 8,'bold'))
        lblSumAss.grid(row = a, column = 1, sticky = W)
        # Label for Summative Assessment
        RSumAss = Radiobutton(self, variable = self.varTypeOfAss, value = 2)
        RSumAss.grid(row = a, column= 1, sticky = NE)
        a = a + 1
        # RadioButton for choosing Summative Assessment

                      
         
        c = 0 # Pointer for txtAns and radbtn
        self.lblQues = [] # Label list for Question
        self.txtQues = [] # Empty Textbox list for Question
        self.radbtn = [] # Radio Button list on the form
        self.txtAns = [] # Textbox list for each answer on the form
        self.btnclear = [] # Button clear list on each question

        self.AnsQues = [None] * 5
#==================================================================================================================
        for Ques in range(5):
            self.AnsQues[Ques] = IntVar()
            self.lblQues.append(Label(self, text = "Question" + str(Ques + 1) + ":"))
            self.lblQues[Ques].grid(row = a, column = 0, sticky = N)
            self.txtQues.append(Text(self, height = 0, width = 40))
            self.txtQues[Ques].grid(row = a, column = 1)
            a = a + 1   
            # Creating Labels and textboxs for each question         
            for choose in range(4):
                self.radbtn.append(Radiobutton(self, variable = self.AnsQues[Ques], value = choose))
                self.radbtn[c].grid(row = a, column = 0, sticky=E)                
                self.txtAns.append(Text(self, height = 0, width = 20))
                self.txtAns[c].grid(row = a, column = 1, sticky = NW)
                a = a + 1
                c = c + 1
                # Creating radio buttons and textboxs for each choose in one question
            self.btnclear.append(Button(self, text = "Clear"))
            self.btnclear[Ques]["command"] = self.clearQues()
            self.btnclear[Ques].grid(row = a - 1, column = 2)
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
        for ques in range(0, len(self.AnsQues)):
            self.AnsQues[ques].set(-1)
        #Empty all choose
#===================================================================================================================

    def clearQues(self):
        #Clear everything in one of the question

        pass
        #End clearQues()

    def storeResponse(self):
        #Store all content
        pass
        #End storeResponse()

    def clearResponse(self):
        #Clear everything on the form           
        self.varTypeOfAss.set(-1)
        for ques in range(0, len(self.AnsQues)):
            self.AnsQues[ques].set(-1)
            self.txtQues[ques].delete(1.0, END)
        for i in range(0, len(self.txtAns)):
            self.txtAns[i].delete(1.0, END)        
        pass
        #End clearResponse()

def Run():
	#Run the program
	root = tk.Tk()
	app = Application(root)
	root.mainloop()

Run() # Run the program