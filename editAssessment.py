from tkinter import *
import tkinter.messagebox as messagebox
from editAssessmentCSV import assessmentCSV, assessmentCSVRead
import datetime

class ChooseAssessment:

    def __init__(self, root):
        root.geometry("300x100")
        root.rowconfigure(0, weight = 1)
        root.columnconfigure(0, weight = 1)
        root.title("Edit Test")
        self.assessmentList = assessmentCSVRead().data
        self.titleList = [title[0] for title in self.assessmentList[0::6]]
        self.frame = Frame(root)
        self.frame.grid()
        self.testChoice(root)
    
    def testChoice(self, root):
        lblTitle = Label(self.frame, text="Select Test to Edit", font=("MS", 12, "bold"))
        lblTitle.grid(row=0, column=0, columnspan=3)

        try:
            lblSelected = Label(self.frame, text="Test:", font=("MS", 10))
            lblSelected.grid(row=1, column=0, pady=10)

            selectedTest = StringVar(self.frame)
            selectedTest.set(self.titleList[0])
            optTest = OptionMenu(self.frame, selectedTest, *self.titleList)
            optTest.grid(row = 1, column = 1, sticky = W)

            butSelect = Button(self.frame, text="Select")
            butSelect["command"]=lambda: self.typeChosen(root, selectedTest)
            butSelect.grid(row = 4, column = 0, columnspan=3)
        except IndexError:
            lblError = Label(self.frame, text="There is no tests in assessments.csv", font=("MS", 10))
            lblError.grid(row=1, column=0, columnspan=3)

    def typeChosen(self, root, index):
        index = self.indexDecode(index.get())
        self.frame.destroy()
        Assessment(root, self.assessmentList[index:index+6], index)

    def indexDecode(self, index):
        for i, x in enumerate(self.assessmentList):
            if index in x:
                return i

class Assessment:

    def __init__(self, root, oldData, CSVIndex):
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
        root.title("Edit " + oldData[0][0])

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
        self.oldData = oldData
        self.CSVIndex = CSVIndex
        self.data = {}
        self.data["assessmentType"] = oldData[2][0]
        self.data["tutorID"] = oldData[1][0]
        self.baseRow = 0
        self.Module = ["CM1202", "CM1210", "CM1208", "CM1120"]
        self.Day = [x for x in range(1, 32)]
        self.Month = [x for x in range(1, 13)]
        self.Year = [x for x in range(2019, 2021)]
        self.fontBold = ("MS", 8, "bold")
        self.fontTitle = ("MS", 12, "bold")
        self.fontText = ("MS", 10)    

        # And here we are, the process of creating the content for creating the assessments
        self.metaWidgets()
        self.createWidgets()

        #End _init_   

    # This idea was again taken from:
    # https://stackoverflow.com/questions/47152542/tkinter-canvas-scrollbar-with-grid
    def reset_scrollregion(self, event):
        self.canvasScroll.config( scrollregion=self.canvasScroll.bbox("all"))

    def metaWidgets(self):
        lblTitle = Label(self.widgetFrame, text = "Edit "+ self.data["assessmentType"] +" Test", font = self.fontTitle)
        lblTitle.grid(row = 0, column = 0, rowspan = 3, columnspan = 3, pady = 20)

        self.baseRow += 3

        lblTestName = Label(self.widgetFrame, text = "Test Name:", font = self.fontText)
        lblTestName.grid(row = self.baseRow, column = 0, pady = 5, padx = 20, sticky = E)

        self.data["testName"] = Text(self.widgetFrame, height = 1, width = 40)
        self.data["testName"].grid(row = self.baseRow, column = 1)
        self.data["testName"].insert(END, self.oldData[0][0])

        self.baseRow += 1

        lblModule = Label(self.widgetFrame, text = "Module:", font = self.fontText)
        lblModule.grid(row = self.baseRow, column = 0, pady = 5, padx = 20, sticky = E)

        self.data["testModule"] = StringVar(self.widgetFrame)
        self.data["testModule"].set(self.oldData[3][0])
        optModule = OptionMenu(self.widgetFrame, self.data["testModule"], *self.Module)
        optModule.grid(row = self.baseRow, column = 1, sticky = W)

        self.baseRow += 4

        lblDate = Label(self.widgetFrame, text = "Due Date:", font = self.fontText)
        lblDate.grid(row = self.baseRow, column = 0, pady = 5, columnspan=2)

        self.baseRow += 1

        lblDay = Label(self.widgetFrame, text = "Day:", font = self.fontText)
        lblDay.grid(row = self.baseRow, column = 0, pady = 5, padx = 20, sticky = E)

        self.data["day"] = IntVar(self.widgetFrame)
        self.data["day"].set(int(self.oldData[4][0][:2]))
        optDay = OptionMenu(self.widgetFrame, self.data["day"], *self.Day)
        optDay.grid(row = self.baseRow, column = 1, sticky = W)

        self.baseRow += 1

        lblMonth = Label(self.widgetFrame, text = "Month:", font = self.fontText)
        lblMonth.grid(row = self.baseRow, column = 0, pady = 5, padx = 20, sticky = E)
        
        self.data["month"] = IntVar(self.widgetFrame)
        self.data["month"].set(int(self.oldData[4][0][3:5]))
        optMonth = OptionMenu(self.widgetFrame, self.data["month"], *self.Month)
        optMonth.grid(row = self.baseRow, column = 1, sticky = W)

        self.baseRow += 1

        lblYear = Label(self.widgetFrame, text = "Year:", font = self.fontText)
        lblYear.grid(row = self.baseRow, column = 0, pady = 5, padx = 20, sticky = E)
        
        self.data["year"] = IntVar(self.widgetFrame)
        self.data["year"].set(int(self.oldData[4][0][6:]))
        optDay = OptionMenu(self.widgetFrame, self.data["year"], *self.Year)
        optDay.grid(row = self.baseRow, column = 1, sticky = W)

        self.baseRow += 1

    def createWidgets(self):

        lblDict = {}
        btnDict = {} # Radio Button list on the form

#==================================================================================================================
        for Ques in range(1, 11):
            lblDict[f"ques{Ques}"] = (Label(self.widgetFrame, text = "Question " + str(Ques) + ":", font = self.fontText))
            lblDict[f"ques{Ques}"].grid(row = self.baseRow, column = 0, pady = 5, padx = 20, sticky = E)
            self.data[f"question{Ques}"] = Text(self.widgetFrame, height = 1,width = 40)
            self.data[f"question{Ques}"].grid(row = self.baseRow, column = 1)
            self.data[f"question{Ques}"].insert(END, self.oldData[0][Ques])
            self.baseRow += 1   
            # Creating Labels and textboxs for each question     
            self.data[f"question{Ques}Correct"] = IntVar()
            self.data[f"question{Ques}Correct"].set(self.oldData[5][Ques])
            for Opt in range(1, 5):
                btnDict[f"but{Ques}Rad"] = Radiobutton(self.widgetFrame, variable = self.data[f"question{Ques}Correct"], value = Opt)
                btnDict[f"but{Ques}Rad"].grid(row = self.baseRow, column = 0, sticky=E)                
                self.data[f"question{Ques}Ans{Opt}"] = Text(self.widgetFrame, height = 0, width = 20)
                self.data[f"question{Ques}Ans{Opt}"].grid(row = self.baseRow, column = 1, sticky = NW)
                self.data[f"question{Ques}Ans{Opt}"].insert(END, self.oldData[Opt][Ques])
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
        error = []
        try:
            self.data['date'] = datetime.date(self.data['year'].get(),self.data['month'].get(),self.data['day'].get())
        except ValueError:
            error.append('Not a valid date')
        else:
            if self.data['date'] <= datetime.datetime.today().date():
                error.append('Enter in a furture date')
            else:
                self.data['date'] = self.data['date'].strftime("%d-%m-%Y")
        for key in self.data:
            if key != 'assessmentType' and key != 'tutorID':
                if str(type(self.data[key])) == "<class 'tkinter.Text'>" and len(self.data[key].get('1.0', END)) == 1:
                    if key == 'testName':
                        error.append('Test Name is not filled in')
                    elif 'question' in key and 'Ans' not in key and len(key) == 9:
                        error.append('Question ' + key[8] + ' is not filled in')
                    elif 'question' in key and 'Ans' in key and len(key) == 13:
                        error.append('Question ' + key[8] + ' Answer ' + key[12] + ' is not filled in')
                    elif 'question' in key and 'Ans' not in key:
                        error.append('Question ' + key[8] + key[9] + ' is not filled in')
                    elif 'question' in key and 'Ans' in key:
                        error.append('Question ' + key[8] + key[9] + ' Answer ' + key[13] + ' is not filled in')
                elif str(type(self.data[key])) == "<class 'tkinter.IntVar'>":
                    if self.data[key].get() == 0 and key[9] == '0':
                        error.append('Question ' + key[8] + key[9] + " doesn't have an answer")
                    elif self.data[key].get() == 0:
                        error.append('Question ' + key[8] + " doesn't have an answer")
        if len(error) == 0:
            assessmentCSV(self.data.copy(), self.CSVIndex)
        else:
            errorMessage = ''
            for x in error:
                errorMessage = errorMessage + '\n' + x
            messagebox.showerror('Test not completed', errorMessage)
        #End storeResponse()

    def clearResponse(self):
        #Clear everything on the form
        self.data["testName"].delete('1.0', END)
        self.data["testModule"] = StringVar(self.widgetFrame)
        self.data["testModule"].set(self.Module[0])
        for Ques in range(1, 11):
            self.data[f"question{Ques}"].delete('1.0', END)
            self.data[f"question{Ques}Correct"].set(0)
            for Opt in range(1, 5):
                self.data[f"question{Ques}Ans{Opt}"].delete('1.0', END)
        #End clearResponse()
		
if __name__ == '__main__':
	root = Tk()
	app = ChooseAssessment(root)
	root.mainloop()
