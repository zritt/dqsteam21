import csv
import tkinter.messagebox as messagebox
from tkinter import END
import sys

class assessmentCSVRead:

    def __init__(self):
        self.location = 'assessments.csv'
        self.data = self.openFile()

    def openFile(self):
        try: 
            with open(self.location, mode='r', newline='') as csv_file:
                return self.readData(csv_file)
        except FileNotFoundError:
            messagebox.showerror('assessments.csv is missing!', 
            'System cannot find assessments.csv. Please make sure it exists.')
            sys.exit()

    def readData(self, csv_file):
        return self.newLineClear(csv_file.readlines())

    def newLineClear(self, array):
        for index in range(len(array)):
            array[index] = array[index].rstrip().split(',')
        return array

class assessmentCSV:

    def __init__(self, data, index):
        self.data = data
        self.location = 'assessments.csv'
        self.oldData = assessmentCSVRead().data
        print(self.oldData)
        self.index = index
        self.decodeData()
        self.openFile()

    def decodeData(self):
        for key in self.data:
            if str(type(self.data[key])) == "<class 'tkinter.Text'>":
                self.data[key] = self.data[key].get('1.0', END).rstrip()
            elif str(type(self.data[key])) == "<class 'tkinter.IntVar'>":
                self.data[key] = self.data[key].get()
            elif str(type(self.data[key])) == "<class 'tkinter.StringVar'>":
                self.data[key] = str(self.data[key].get())
                      
    def openFile(self):
        try:
            with open(self.location, mode = 'w', newline='') as csv_file:
                self.storeData(csv_file)
        except FileNotFoundError:
            messagebox.showerror('assessments.csv is missing!', 
            'System cannot find assessments.csv. Please make sure it exists.')
            sys.exit()

    def storeData(self, csv_file):
        self.oldData[self.index] = [self.data['testName'], self.data['question1'], self.data['question2'], self.data['question3'], self.data['question4'], self.data['question5'], self.data['question6'], self.data['question7'], self.data['question8'], self.data['question9'], self.data['question10']]
        self.oldData[self.index+1] = [self.data['tutorID'], self.data['question1Ans1'], self.data['question2Ans1'], self.data['question3Ans1'], self.data['question4Ans1'], self.data['question5Ans1'], self.data['question6Ans1'], self.data['question7Ans1'], self.data['question8Ans1'], self.data['question9Ans1'], self.data['question10Ans1']]
        self.oldData[self.index+2] = [self.data['assessmentType'], self.data['question1Ans2'], self.data['question2Ans2'], self.data['question3Ans2'], self.data['question4Ans2'], self.data['question5Ans2'], self.data['question6Ans2'], self.data['question7Ans2'], self.data['question8Ans2'], self.data['question9Ans2'], self.data['question10Ans2']]
        self.oldData[self.index+3] = [self.data['testModule'], self.data['question1Ans3'], self.data['question2Ans3'], self.data['question3Ans3'], self.data['question4Ans3'], self.data['question5Ans3'], self.data['question6Ans3'], self.data['question7Ans3'], self.data['question8Ans3'], self.data['question9Ans3'], self.data['question10Ans3']]
        self.oldData[self.index+4] = [self.data['date'], self.data['question1Ans4'], self.data['question2Ans4'], self.data['question3Ans4'], self.data['question4Ans4'], self.data['question5Ans4'], self.data['question6Ans4'], self.data['question7Ans4'], self.data['question8Ans4'], self.data['question9Ans4'], self.data['question10Ans4']]
        self.oldData[self.index+5] = ['', self.data['question1Correct'], self.data['question2Correct'], self.data['question3Correct'], self.data['question4Correct'], self.data['question5Correct'], self.data['question6Correct'], self.data['question7Correct'], self.data['question8Correct'], self.data['question9Correct'], self.data['question10Correct']]
        assessmentWriter = csv.writer(csv_file, delimiter=',')
        assessmentWriter.writerows(self.oldData)
