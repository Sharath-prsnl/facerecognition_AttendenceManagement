import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
import csv



def display(e2):
    found = ""
    key = str(e2.get())
    
    csv_file = csv.reader(open('Attendance\Attendance_2021-05-23.csv', "r"), delimiter=",")
    print(key)
    print("AFTER csv")
    for row in csv_file:
        print(row[0])
        if key == row[0]:
            found += str(row)
            print(found)
    root = Tk()
    root.title('Search Result') 
    root.geometry("400x400")
    if len(found)>0:
        label = Label(root, text= found)
        label.pack()
    else:
        label = Label(root, text="Student Not Found")
        label.pack()
    root.mainloop()