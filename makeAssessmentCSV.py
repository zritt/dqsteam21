import csv
import tkinter.messagebox as messagebox
from tkinter import END
import sys

class assessmentCSV:

    def __init__(self, data):
        self.data = data
        self.location = 'assessment.csv'
        self.decodeData()
        self.openFile()

    def decodeData(self):
        print(self.data['testModule'])
        print(type(self.data['testModule']))
        print(self.data['testModule'].get())
        for key in self.data:
            if str(type(self.data[key])) == "<class 'tkinter.Text'>":
                self.data[key] = self.data[key].get('1.0', END).rstrip()
            elif str(type(self.data[key])) == "<class 'tkinter.IntVar'>":
                self.data[key] = self.data[key].get()
            elif str(type(self.data[key])) == "<class 'tkinter.StringVar'>":
                print("it's doing this")
                self.data[key] = str(self.data[key].get())
                      
    def openFile(self):
        try:
            with open(self.location, mode = 'a', newline='') as csv_file:
                self.storeData(csv_file)
        except FileNotFoundError:
            messagebox.showerror('assessment.csv is missing!', 
            'System cannot find assessment.csv. Please make sure it exists.')
            sys.exit()

    def storeData(self, csv_file):
        row1 = [self.data['testName'], self.data['question1'], self.data['question2'], self.data['question3'], self.data['question4'], self.data['question5'], self.data['question6'], self.data['question7'], self.data['question8'], self.data['question9'], self.data['question10']]
        row2 = [self.data['tutorID'], self.data['question1Ans1'], self.data['question2Ans1'], self.data['question3Ans1'], self.data['question4Ans1'], self.data['question5Ans1'], self.data['question6Ans1'], self.data['question7Ans1'], self.data['question8Ans1'], self.data['question9Ans1'], self.data['question10Ans1']]
        row3 = [self.data['assessmentType'], self.data['question1Ans2'], self.data['question2Ans2'], self.data['question3Ans2'], self.data['question4Ans2'], self.data['question5Ans2'], self.data['question6Ans2'], self.data['question7Ans2'], self.data['question8Ans2'], self.data['question9Ans2'], self.data['question10Ans2']]
        row4 = [self.data['testModule'], self.data['question1Ans3'], self.data['question2Ans3'], self.data['question3Ans3'], self.data['question4Ans3'], self.data['question5Ans3'], self.data['question6Ans3'], self.data['question7Ans3'], self.data['question8Ans3'], self.data['question9Ans3'], self.data['question10Ans3']]
        row5 = ['', self.data['question1Ans4'], self.data['question2Ans4'], self.data['question3Ans4'], self.data['question4Ans4'], self.data['question5Ans4'], self.data['question6Ans4'], self.data['question7Ans4'], self.data['question8Ans4'], self.data['question9Ans4'], self.data['question10Ans4']]
        row6 = ['', self.data['question1Correct'], self.data['question2Correct'], self.data['question3Correct'], self.data['question4Correct'], self.data['question5Correct'], self.data['question6Correct'], self.data['question7Correct'], self.data['question8Correct'], self.data['question9Correct'], self.data['question10Correct']]
        rows = [row1, row2, row3, row4, row5, row6]
        print(row4)
        assessmentWriter = csv.writer(csv_file, delimiter=',')
        assessmentWriter.writerows(rows)
