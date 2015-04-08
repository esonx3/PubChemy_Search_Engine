#!/usr/bin/python
# -*- coding: latin-1 -*-

# PubChemPy Graphical Client using Tkinter
# By: Grupp 11

from Tkinter import *

root = Tk()

# create Frame
frame = Frame()
frame.pack()

#temporery command to test functions
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

def open_file(self):
    fname = askopenfilename(filetypes=(("Template files", "*.tplate"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*") ))

def search(event):
    print E.get()
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
C = Canvas(root, bg="white", bd=4, width=355, height=300, relief=GROOVE)
C.pack()
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
filemenu.add_command(label="Save", command=hello) #change command to "save file"
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

historymenu = Menu(menubar, tearoff=0)
historymenu.add_command(label="Latest Search", command=hello)
historymenu.add_command(label="Random function", command=hello)
menubar.add_cascade(label="History", menu=historymenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about) #change command to print instructions in window
menubar.add_cascade(label="Help", menu=helpmenu)


# display the menu
root.config(menu=menubar)
mainloop()