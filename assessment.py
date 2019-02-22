from tkinter import *

class Assessment:

    def __init__(self, root, assessmentType):
        #Form GUI
        # Explaination for this section:
        # Tkinter doesn't like scrollbars in Frames, humans don't like widgets in Canvases
        # This means that in the Init there will be a structure of: Frame (The window itself) --> Canvas (For the Scrollbar) --> Frame (For the widgets)
        # It's a pain in the bottom, but hopefully it'll be automated to the point where none of you will have to care
        # - love, Kai
        root.maxsize(1920, 1080)
        
        self.windowFrame = Frame(root)
        self.windowFrame.grid()
        self.windowFrame.grid_columnconfigure(0, weight = 1)
        self.windowFrame.grid_rowconfigure(0, weight = 1)

        self.canvasScroll = Canvas(self.windowFrame)
        self.canvasScroll.grid(row = 0, column = 0, sticky = NSEW)

        self.widgetFrame = Frame(self.canvasScroll)
        self.widgetFrame.grid(row = 0, column = 0, sticky = NSEW)
        self.canvasScroll.create_window(0, 0, anchor = NW, window= self.widgetFrame)

        #This is the far less stressful part where I define some variables for later use. These are used to keep 

        self.scrollbar = Scrollbar(self.windowFrame,
                                    command = self.canvasScroll.yview)
        self.scrollbar.grid(row = 0, column = 1, sticky = NS)

        self.createWidgets()

        #This command is after we create all the widgets, as python still runs it before the user sees anything. All it does is make the scroll region 


        #End _init_   


    def createWidgets(self):
        lblFirstLine = Label(self.widgetFrame, text = "Create test", font = ("MS", 12,"bold"))
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
            lblQues.append(Label(self.widgetFrame, text = "Question" + str(Ques + 1) + ":"))
            lblQues[Ques].grid(row = a, column = 0, padx = 10)
            txtQues.append(Text(self.widgetFrame, height = 1,width = 40))
            txtQues[Ques].grid(row = a, column = 1)
            a = a + 1   
            # Creating Labels and textboxs for each question         
            for choose in range(4):
                radbtn.append(Radiobutton(self.widgetFrame, variable = self.AnsQues[Ques], value = choose))
                radbtn[c].grid(row = a, column = 0, sticky=E)                
                txtAns.append(Text(self.widgetFrame, height = 0, width = 20))
                txtAns[c].grid(row = a, column = 1, sticky = NW)
                a = a + 1
                c = c + 1
                # Creating radio buttons and textboxs for each choose in one question
            btnclear.append(Button(self.widgetFrame, text = "Clear"))
            btnclear[Ques]["command"] = self.clearQues
            btnclear[Ques].grid(row = a - 1, column = 2)
            # Creating clear button for each question
        #End loop for creating every question with chooses
#===================================================================================================================
        btnSubmit = Button(self.widgetFrame, text = "Submit")
        btnSubmit["command"] = self.storeResponse
        btnSubmit.grid(row = a, column = 1, sticky = W) 
        #Submit button
        btnClearAll = Button(self.widgetFrame, text = "Clear All")
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
	root = Tk()
	app = Assessment(root, 'Test')
	root.mainloop()


if __name__ == "__main__":
    Run() # Run the program