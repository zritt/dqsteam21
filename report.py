from tkinter import *
import tkinter.ttk as ttk
import csv
import itertools


class Report(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title('Report')
        width = 1100
        height = 400
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        master.resizable(0, 0)


        TableMargin = Frame(master, width=500)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("StudentID", "Firstname", "Lastname", "Testname", "Score"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('StudentID', text="Student ID", anchor=W)
        tree.heading('Firstname', text="Firstname", anchor=W)
        tree.heading('Lastname', text="Lastname", anchor=W)
        tree.heading('Testname', text="Testname", anchor=W)
        tree.heading('Score', text="Score", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=200)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=300)
        tree.pack()


        f1 = open('students.csv')
        f2= open('results.csv')
        csv_f1 = csv.DictReader(f1, delimiter=',')
        csv_f2 = csv.DictReader(f2, delimiter=',')

        for row2, row1 in itertools.zip_longest(csv_f2, csv_f1):
            if row2['Student ID'] == row1['stud id']:
                Firstname = row1['first name']
                Lastname = row1['last name']
                StudentID = row2['Student ID']
                Testname = row2['Test Name']
                Score = row2['Score']
                tree.insert("", 0, values=(StudentID, Firstname, Lastname, Testname, Score))






if __name__ == "__main__":
    root = Tk()
    root.title("Report")
    app = Report(root)
    root.mainloop()
