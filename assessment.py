from tkinter import *
#mport tkinter as Tk

class Assessmentfrom tkinter import *

class Assessment:

    def __init__(self, root, assessmentType):
        #Form GUI
        # Explaination for this section:
        # Tkinter doesn't like scrollbars in Frames, humans don't like widgets in Canvases
        # This means that in the Init there will be a structure of: Frame (The window itself) --> Canvas (For the Scrollbar) --> Frame (For the widgets)
        # But you also have to take the root into account. So there's 4 layers of containers before any actual content.

        # Many ideas used in this section of code are adapted from:
        # https://stackoverflow.com/questions/47152542/tkinter-canvas-scrollbar-with-grid

        # These lines simply set up the root. Geometry sets the default window size.  
        # Row / Column configure mean that row = 0 and column = 0 will be given a priority (or weight) over the other rows and columns. 
        # As there are nothing in the root but windowFrame, that means it expands to fill the whole root.
        root.geometry("500x648")
        root.rowconfigure(0, weight = 1)
        root.columnconfigure(0, weight = 1)
        root.title("Create " + assessmentType + " Test")

        self.windowFrame = Frame(root)
        self.windowFrame.grid(sticky = NSEW)
        
        self.windowFrame.columnconfigure(0, weight = 1)
        self.windowFrame.rowconfigure(0, weight = 1)

        self.canvasScroll = Canvas(self.windowFrame)
        self.canvasScroll.grid(row = 0, column = 0, sticky = NSEW)

        self.scrollbar = Scrollbar(self.windowFrame, command = self.canvasScroll.yview)
        self.scrollbar.grid(row = 0, column = 1, sticky = NS)
        self.canvasScroll.config(yscrollcommand = self.scrollbar.set)

        self.widgetFrame = Frame(self.canvasScroll)
        self.widgetFrame.columnconfigure(1, weight = 1)
        self.widgetFrame.rowconfigure(1, weight = 1)
        self.canvasScroll.create_window(0, 0, anchor = NW, window= self.widgetFrame)
        self.widgetFrame.bind("<Configure>", self.reset_scrollregion)
        
        #This is the far less stressful part where I define some variables for later use. These are used to keep 

        self.data = {}
        self.data["AssessmentType"] = assessmentType
        self.baseRow = 0
        self.cohort = ["CM1202", "CM1210", "CM1208", "CM1120"]
        self.fontBold = ("MS", 8, "bold")
        self.fontTitle = ("MS", 12, "bold")
        self.fontText = ("MS", 10)


        # And here we are, the process of creating the content for creating the assessments
        self.metaWidgets()
        if assessmentType == "Formative":
            self.formativeWidgets()
        elif assessmentType == "Summative":
            self.summativeWidgets()
        else:
            print("Test Mode Selected")
        self.createWidgets()

        #End _init_   

    # This idea was again taken from:
    # https://stackoverflow.com/questions/47152542/tkinter-canvas-scrollbar-with-grid
    def reset_scrollregion(self, event):
        self.canvasScroll.config( scrollregion=self.canvasScroll.bbox("all"))

    def metaWidgets(self):
        lblTitle = Label(self.widgetFrame, text = "Create "+ self.data["AssessmentType"] +" Test", font = self.fontTitle)
        lblTitle.grid(row = 0, column = 0, rowspan = 3, columnspan = 3, pady = 20)

        self.baseRow += 3

        lblTestName = Label(self.widgetFrame, text = "Test Name:", font = self.fontText)
        lblTestName.grid(row = self.baseRow, column = 0, pady = 5, padx = 20, sticky = E)

        self.data["testName"] = Text(self.widgetFrame, height = 1, width = 40)
        self.data["testName"].grid(row = self.baseRow, column = 1)

        self.baseRow += 1

        lblCohort = Label(self.widgetFrame, text = "Cohort:", font = self.fontText)
        lblCohort.grid(row = self.baseRow, column = 0, pady = 5, padx = 20, sticky = E)

        default = StringVar(self.widgetFrame)
        default.set(self.cohort[0])
        self.data["testCohort"] = OptionMenu(self.widgetFrame, default, *self.cohort)
        self.data["testCohort"].grid(row = self.baseRow, column = 1, sticky = W)


        self.baseRow += 4

    def formativeWidgets(self):
        pass

    def summativeWidgets(self):
        pass

    def createWidgets(self):

        lblDict = {}
        btnDict = {} # Radio Button list on the form

#==================================================================================================================
        for Ques in range(1, 11):
            lblDict[f"ques{Ques}"] = (Label(self.widgetFrame, text = "Question " + str(Ques) + ":", font = self.fontText))
            lblDict[f"ques{Ques}"].grid(row = self.baseRow, column = 0, pady = 5, padx = 20, sticky = E)
            self.data[f"question{Ques}"] = Text(self.widgetFrame, height = 1,width = 40)
            self.data[f"question{Ques}"].grid(row = self.baseRow, column = 1)
            self.baseRow += 1   
            # Creating Labels and textboxs for each question     
            self.data[f"question{Ques}Correct"] = IntVar()
            for Opt in range(1, 5):
                
                btnDict[f"but{Ques}Rad"] = Radiobutton(self.widgetFrame, variable = self.data[f"question{Ques}Correct"], value = Opt)
                btnDict[f"but{Ques}Rad"].grid(row = self.baseRow, column = 0, sticky=E)                
                self.data[f"question{Ques}Ans{Opt}"] = Text(self.widgetFrame, height = 0, width = 20)
                self.data[f"question{Ques}Ans{Opt}"].grid(row = self.baseRow, column = 1, sticky = NW)
                self.baseRow += 1
                # Creating radio buttons and textboxs for each choose in one question
            btnDict[f"but{Ques}Clear"] = Button(self.widgetFrame, text = "Clear")
            btnDict[f"but{Ques}Clear"]["command"] = lambda Ques = Ques:  self.clearQues(Ques)
            btnDict[f"but{Ques}Clear"].grid(row = self.baseRow - 1, column = 2)
            # Creating clear button for each question
        #End loop for creating every question with chooses
#===================================================================================================================
        btnDict[f"butSubmit"] = Button(self.widgetFrame, text = "Submit")
        btnDict[f"butSubmit"]["command"] = self.storeResponse
        btnDict[f"butSubmit"].grid(row = self.baseRow, column = 1, sticky = W) 
        #Submit button
        btnDict[f"butClear"] = Button(self.widgetFrame, text = "Clear All")
        btnDict[f"butClear"]["command"] = self.clearResponse
        btnDict[f"butClear"].grid(row = self.baseRow, column = 1, sticky = N)
        #ClearAll button
        #End createWidgets()
#===================================================================================================================

    def clearQues(self, Ques):
        #Clear everything in one of the question
        self.data[f"question{Ques}"].delete('1.0', END)
        self.data[f"question{Ques}Correct"].set(0)
        for Opt in range(1, 5):
            self.data[f"question{Ques}Ans{Opt}"].delete('1.0', END)
        #End clearQues()

    def storeResponse(self):
        #Store all content
        for key in self.data:
            if key != 'AssessmentType':
                print(type(self.data[key]))
        #End storeResponse()

    def clearResponse(self):
        #Clear everything on the form
        for Ques in range(1, 11):
            self.data[f"question{Ques}"].delete('1.0', END)
            self.data[f"question{Ques}Correct"].set(0)
            for Opt in range(1, 5):
                self.data[f"question{Ques}Ans{Opt}"].delete('1.0', END)
        #End clearResponse()

def Run():
	#Run the program
    root = Tk()
    app = Assessment(root, 'Test')
    root.mainloop()


if __name__ == "__main__":
    Run() # Run the program(Frame):
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