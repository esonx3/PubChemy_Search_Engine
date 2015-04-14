#!/usr/bin/python
# -*- coding: latin-1 -*-

# PubChemPy Graphical Client using Tkinter
# By: Grupp 11

from Tkinter import *
from tkFileDialog import askopenfilename
def search_log():
    about()

def onKey(event):
    print "Key relesed!"#, inStr
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
    open_file()

def get_Last_key(event):
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

    C.insert('1.0', separator2.get() + '\n')
    C.image_create('1.0', image=img2)
    if B.cget("state"):
        print B.cget("state"), "E.get"
    else:
        print "Disabled!"
    if get_Last_key(event) == 0:
        separator2.delete(0, END)
    # 4 now for testing only...
    #print E.get(), "E.get"


def GO_name(name):
    sometext=str(E.get())
    B.config(text='Loading...')
    #cid=get_compounds(name,'name')
    #comp = Compound.from_cid(cid)
    #result.config(text=str(comp.isomeric_smiles))
    C.config(bg='grey')
    #return comp.isomeric_smiles


class CreateButton:
    def Small(self, varb):
        f1 = Frame(topbar, height=24, width=24)
        f1.pack_propagate(0) # don't shrink
        f1.pack(side=LEFT)
        b1 = Button(f1, image=self.img2)
        b1.pack(fill=BOTH, expand=1)
        b1.bind('<Button-1>', lambda(e): search(varb))

    def __init__(self, varb):
        self.img2 = PhotoImage(file="firefox_icon.gif")
        self.Small(varb)




root = Tk()
# top create Frame
topbar = Frame(height=300)
topbar.pack(fill=X)


#creat 2:nd frame
frame = Frame()
frame.pack(fill=X)
#creat an scrollbar to the frame
scrollbar = Scrollbar(frame)

img2 = PhotoImage(file="firefox_icon.gif")

#TODO is thi needed?
#topbar_line = Frame(height=2, bd=1, relief=SUNKEN)
#topbar_line.pack(fill=X, padx=5, pady=5)
#separator = Frame(height=2, bd=1, relief=SUNKEN)
#separator.pack(fill=X, padx=5, pady=5)

#text area for output
C = Text(frame, bg="white", wrap=WORD, yscrollcommand=scrollbar.set)
#C.insert(INSERT, "\n\nhello world")#hello world...
#scrollbar till outpot text
scrollbar.config(command=C.yview)
scrollbar.pack(side=RIGHT,  fill=Y)
C.config(yscrollcommand=scrollbar.set)
C.pack(side="left", fill=X, expand=True)

#TODO is this needed?
#txt = Text(frame, height=15, width=55)
#scr = Scrollbar(frame)
#scrollbar.pack(side="right", fill="y", expand=False) // not needed?

# Entry widget
separator2 = Entry(relief=SUNKEN)
separator2.pack(fill=X, padx=5, pady=5)
separator2.focus()
separator2.bind('<Return>',search)
separator2.bind('<KeyRelease>',onKey) #Does nothing? reacting on key release

#TODO is this needed?
#v = StringVar()
#left = Frame()
#left.pack()
#E = Entry(left,textvariable=v)
#E.focus()

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
#TODO removed the static size, put it back if needed
# display the menu
#root.geometry("400x600") //not needed as the parts in the window got defined sizes
root.config(menu=menubar)
mainloop()