#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *
from pubchempy import *
import CAS_DB

CAS_BDTABASE = CAS_DB.CAS_DB()


#GO key release (this can be a class)
def onKey(event):
    inStr=str(entry.get())
    button.config(state='normal')

def GO_name(name):
    sometext=str(entry.get())
    button.config(text='Loading...')
    #cid=get_compounds(name,'name')
    #comp = Compound.from_cid(cid)
    #result.config(text=str(comp.isomeric_smiles))
    result.config(text=sometext)
    #return comp.isomeric_smiles

def GO_cas(CAS):
    global CAS_BDTABASE
    cid = CAS_BDTABASE.Find_CID_BY_CAS(CAS,True)
    return int(cid[0])

def GO_smiles(SMILES):
    cid=get_compounds(SMILES,'smiles')
    return int(cid[0])

#this should be a class
def get_smiles(cid):
    comp = Compound.from_cid(cid)
    return comp.isomeric_smiles

def get_name(cid):
    comp = Compound.from_cid(cid)
    return comp.name

#def get_cas(cid)


#end of the class

root = Tk()
label = Label(root,text='give CAS number/name/SMILES')
entry = Entry(root)
result= Label(root,text="")
button=Button(text='Send',state='disabled',command=lambda:GO_name(entry))
entry.bind('<KeyRelease>',onKey)

#button.bind('<Button-1>',GO_name(entry))




label.pack()
entry.pack()
button.pack()
result.pack()


#label2=Label(root,GO_name(entry))
#label2.pack()

root.geometry("%dx%d%+d%+d" % (300,150,100,100))

root.mainloop()
