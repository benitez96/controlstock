import tkinter as tk

class Form:
    '''This class gets a Tkinter object and prints a form in it.'''
    
    def __init__(self, topl_obj, title, fields, start_row=0, show_last=False):
        self.window = topl_obj
        self.window.title(title)
        self.window.geometry('200x200')
        self.entry = {}
        for i, field in enumerate(fields, start_row):
            tk.Label(self.window, text=field).grid(row=i, column=0)
            entry = tk.Entry(self.window)
            entry.grid(row=i, column=1)
            self.entry[field] = entry

