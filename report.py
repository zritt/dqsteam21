from tkinter import *
import tkinter.ttk as ttk
import csv
import itertools


class Report(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title('Report')


        f1= open('results.csv')
        csv_f1 = csv.DictReader(f1, delimiter=',')
        f2= open('results.csv')
        csv_f2 = csv.DictReader(f2, delimiter=',')

        def CurSelet(evt):
            value=str((listbox.get(ACTIVE)))
            createtable(value)

        listbox = Listbox(master, height=3)
        scroll = Scrollbar(master, command=listbox.yview)
        listbox.configure(yscrollcommand=scroll.set)


        mylist = []
        mylist.append("All Tests")
        for row2 in csv_f2:
            mylist.append(row2['Test Name'])
        mylist = list(dict.fromkeys(mylist))

        for item in mylist:
            listbox.insert(END, item)

        listbox.select_set(0)
        listbox.event_generate("<<ListboxSelect>>")

        listbox.bind('<<ListboxSelect>>',CurSelet)

        listbox.pack()


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

        def createtable(value):
            for row1 in csv_f1:
                if value == "All Tests":
                    Firstname = row1['FirstName']
                    Lastname = row1['LastName']
                    StudentID = row1['Student ID']
                    Testname = row1['Test Name']
                    Score = row1['Score']
                    tree.insert("", 0, values=(StudentID, Firstname, Lastname, Testname, Score))






    #if listbox.get(ACTIVE) == "All Tests":
