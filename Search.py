import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
import csv
import sys
import Display

def search():
    master = tk.Tk()
    master.title("Search student")
    tk.Label(master, text="Enter Name").grid(row=0)
    tk.Label(master, text="USN").grid(row=1)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    Button(master, text="Search", command=lambda: Display.display(e2)).grid(row=2, column=1, sticky=W, pady=4)
    
    master.geometry("400x400")
    master.mainloop()

