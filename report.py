# This class is for viewing reports of student performance by the tutor

from tkinter import *
import tkinter as tk
import csv

class report(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        pass


root = tk.Tk()
app=report(root)
root.mainloop()
