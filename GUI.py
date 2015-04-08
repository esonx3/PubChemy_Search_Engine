#!/usr/bin/python
# -*- coding: latin-1 -*-

# PubChemPy Graphical Client using Tkinter
# By: Grupp 11

from Tkinter import *
from tkFileDialog import askopenfilename

root = Tk()

# create Frame
frame = Frame()
frame.pack()

#temporery command to test functions

def search_log():
    about()

def onKey(event):
    inStr=str(E.get())
    B.config(state='normal')

def hello():
    print "hello!"

def about():
    top = Toplevel()
    top.title("Python PubChem App")

    msg = Message(top, text="PubChem Client")
    msg.pack()

    button = Button(top, text="Ok", command=top.destroy)
    button.pack()

def open_file():
    name = askopenfilename()

def save_file():
    name = askopenfilename()

def search(event):
    print E.get()
    C.insert('1.0', E.get() + '\n')
    if B.cget("state"):
        print B.cget("state")
    else:
        print "Disabled!"

def GO_name(name):
    sometext=str(E.get())
    B.config(text='Loading...')
    #cid=get_compounds(name,'name')
    #comp = Compound.from_cid(cid)
    #result.config(text=str(comp.isomeric_smiles))
    C.config(bg='grey')
    #return comp.isomeric_smiles

# create a Canvas
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

C = Text(root, bg="white", bd=2, wrap=WORD, yscrollcommand=scrollbar.set)
C.pack()
C.insert(INSERT, "\n\nhello world")


v = StringVar()

# Button
B=Button(frame,state='disabled',command=lambda: GO_name(E),text="GO!",fg="blue",bg="red",width=5)
B.bind('<Button-1>', search)
B.grid(row=1, column=2)

# Entry widget
E = Entry(frame,textvariable=v)
E.grid(row=1, column=1)
E.bind('<Return>',search)
E.bind('<KeyRelease>',onKey)
E.focus()


#create OptionMenu
var2 = StringVar(root)
var2.set("Name") # initial value
option = OptionMenu(frame, var2, "Name", "Smiley", "CAS")
option.grid(row=1, column=0)

# create a toplevel menu
menubar = Menu(root)

# create pulldown menus, and add them to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file) #change command to "read file"
filemenu.add_command(label="Save", command=save_file) #change command to "save file"
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

historymenu = Menu(menubar, tearoff=0)
historymenu.add_command(label="Search log", command=search_log)
historymenu.add_command(label="Random function", command=hello)
menubar.add_cascade(label="History", menu=historymenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about) #change command to print instructions in window
menubar.add_cascade(label="Help", menu=helpmenu)


# display the menu
root.config(menu=menubar)
mainloop()