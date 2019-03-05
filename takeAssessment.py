from tkinter import *
import tkinter as tk
import csv

class takeAssessment(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        pass


root = tk.Tk()
app = takeAssessment(root)
root.mainloop()