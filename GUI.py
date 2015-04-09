#!/usr/bin/python
# -*- coding: latin-1 -*-

# PubChemPy Graphical Client using Tkinter
# By: Grupp 11

from Tkinter import *
from tkFileDialog import askopenfilename

root = Tk()

# create Frame
frame = Frame()
frame.pack(fill=X)
left = Frame()
left.pack()

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
    C.insert('1.0', separator2.get() + '\n')
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


img2 = PhotoImage(file="~/firefox_icon.gif")

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

separator2 = Entry(relief=SUNKEN)
separator2.pack(fill=X, padx=5, pady=5)
separator2.focus()


f1 = Frame(left, height=32, width=32)
f2 = Frame(left, height=32, width=32)
f3 = Frame(left, height=32, width=32)
f1.pack_propagate(0) # don't shrink
f1.pack(side=LEFT)
f2.pack_propagate(0) # don't shrink
f2.pack(side=LEFT)
f3.pack_propagate(0) # don't shrink
f3.pack(side=LEFT)

b1 = Button(f1, image=img2)
b2 = Button(f2, image=img2)
b3 = Button(f3, text="...")

b1.pack(fill=BOTH, expand=1)
b2.pack(fill=BOTH, expand=1)
b3.pack(fill=BOTH, expand=1)


#create OptionMenu
var2 = StringVar(root)
var2.set("Name") # initial value

separator3 = OptionMenu(left, var2, "Name", "Smiley", "CAS")
separator3.pack(fill=X, padx=5, pady=5)

scrollbar = Scrollbar(frame)

C = Text(frame, bg="white", wrap=WORD, yscrollcommand=scrollbar.set)
C.insert(INSERT, "\n\nhello world")
scrollbar.config(command=C.yview)
scrollbar.pack(side=RIGHT, fill=Y)
C.config(yscrollcommand=scrollbar.set)

txt = Text(frame, height=15, width=55)
scr = Scrollbar(frame)

scrollbar.pack(side="right", fill="y", expand=False)
C.pack(side="left", fill=X, expand=True)

v = StringVar()

# Button
B=Button(left,state='disabled',command=lambda: GO_name(E),text="GO!",fg="blue",bg="red",width=5)
B.bind('<Button-1>', search)

# Entry widget
E = Entry(frame,textvariable=v)

separator2.bind('<Return>',search)
separator2.bind('<KeyRelease>',onKey)
E.focus()




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
root.geometry("400x600")

root.config(menu=menubar)
mainloop()