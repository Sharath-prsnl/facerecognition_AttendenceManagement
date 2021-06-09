import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
import csv
import datetime
import time



def display(e2):
    found = []
    key = str(e2.get())
    
    csv_file = csv.reader(open('Attendance\Attendance_'+ datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d') +'.csv', "r"), delimiter=",")
    for row in csv_file:
        print(row[0])
        if key == row[0]:
            found = [i for i in row]

    root = Tk()
    root.title('Search Result') 
    root.geometry("400x400")
    columns = ['Id','Name','Date','Time', 'Department', 'Subject', 'Semester']
    if len(found)>0:
        for i in range(7):
            label = Label(root, text=(columns[i] + ": " + found[i]))
            label.pack()
    else:
        label = Label(root, text="Student Not Found")
        label.pack()
    root.mainloop()