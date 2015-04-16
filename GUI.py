#!/usr/bin/python
# -*- coding: latin-1 -*-

# PubChemPy Graphical Client using Tkinter
# By: Grupp 11

# Program opens Tkinter application that could retrieve information for a public chemistry database

from Tkinter import *
from tkFileDialog import askopenfilename
from pubchempy import *


def search_log():
    about()


def onKey(event):
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
    pass


def get_last_key(event):
    if event == "1":
        print "knapp 1"
        return 1
    elif event == "2":
        print "knapp 2"
        return 2
    elif event == "3":
        print "knapp " + event
        return 3
    else:                       # remove the old text from the "enter window"
        print "enterkey..."
        return 0


def search(event):
    """
    :param event:
    :return:
    """
    var_win_text = get_compounds(separator2.get(), 'name')
    C.insert('1.0', var_win_text)
    C.insert('1.0', "\n")
    if B.cget("state"):
        print B.cget("state"), "E.get"
    else:
        print "Disabled!"
    if get_last_key(event) == 0:
        separator2.delete(0, END)


def go_name(name):
    B.config(text='Loading...')
    C.config(bg='grey')


class CreateButton:
    def small(self, varb):
        f1 = Frame(topbar, height=24, width=24)
        f1.pack_propagate(0)  # don't shrink
        f1.pack(side=LEFT)
        b1 = Button(f1, image=self.img2)
        b1.pack(fill=BOTH, expand=1)
        b1.bind('<Button-1>', lambda(e): search(varb))

    def __init__(self, varb):
        self.img2 = PhotoImage(file="firefox_icon.gif")
        self.small(varb)

root = Tk()
topbar = Frame(height=300)
topbar.pack(fill=X)

# Create 2:nd frame
frame = Frame()
frame.pack(fill=X)
#creat an scrollbar to the frame
scrollbar = Scrollbar(frame)

img2 = PhotoImage(file="firefox_icon.gif")

#text area for output
C = Text(frame, bg="white", wrap=WORD, yscrollcommand=scrollbar.set)
#C.insert(INSERT, "\n\nhello world")#hello world...
#scrollbar till outpot text
scrollbar.config(command=C.yview)
scrollbar.pack(side=RIGHT,  fill=Y)
C.config(yscrollcommand=scrollbar.set)
C.pack(side="left", fill=X, expand=True)

# Entry widget
separator2 = Entry(relief=SUNKEN)
separator2.pack(fill=X, padx=5, pady=5)
separator2.focus()
separator2.bind('<Return>',search)
separator2.bind('<KeyRelease>',onKey) #Does nothing? reacting on key release

#creat buttons
bu1 = CreateButton("1")
bu2 = CreateButton("2")
bu3 = CreateButton("3")

#hiden button, (activated by enter key)
B = Button(topbar,state='disabled',command=lambda: GO_name(E),text="GO!",fg="blue",bg="red",width=5)
B.bind('<Button-1>', search)

#create OptionMenu
var2 = StringVar(root)
var2.set("Name") # initial value
separator3 = OptionMenu(topbar, var2, "Name", "Smiley", "CAS")
separator3.pack(fill=X, padx=5, pady=5)

# create a toplevel menu
menubar = Menu(root)
# create pulldown menus, and add them to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file)  # change command to "read file"
filemenu.add_command(label="Save", command=save_file)  # change command to "save file"
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

historymenu = Menu(menubar, tearoff=0)
historymenu.add_command(label="Search log", command=search_log)
historymenu.add_command(label="Random function", command=hello)
menubar.add_cascade(label="History", menu=historymenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)  #change command to print instructions in window
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)
mainloop()