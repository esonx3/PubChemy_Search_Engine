#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *
from pubchempy import *
import CAS_DB

CAS_BDTABASE = CAS_DB.CAS_DB()


def onKey(event):
    inStr=str(entry.get())
    button.config(state='normal')

def name_to_CID(name):
    result0.config(text="")    
    #button.config(text='Loading...')
    sometext=str(entry.get())
    try:
        
        cid=get_compounds(sometext,'name')
        CID_to_name(cid)
        CID_to_smiles(cid)
    except:
        result0.config(text="Your compound most probably doesn't exist")

def smiles_to_CID(SMILES):
    result0.config(text="")
    sometext=str(entry.get())
    try:
        cid=get_compounds(sometext,'smiles')
        CID_to_name(cid)
        CID_to_smiles(cid)
    except:
        result0.config(text="Your compound most probably doesn't exist")

#global CAS_BDTABASE
#cas=str(raw_input('give a cas: '))
##cid=get_compounds(smiles,'smiles')
#cid = CAS_BDTABASE.Find_CID_BY_CAS(cas,True)
#print 'cid: ' + str(cid)


def cas_to_CID(CAS):
    global CAS_BDTABASE
    cid = CAS_BDTABASE.Find_CID_BY_CAS(CAS,True)
#    return int(cid[0])
    CID_to_name(cid)
    CID_to_smiles(cid)

def CID_to_smiles(cid):
    SMILES_all=[]
    number_of_compounds=len(cid)
    for i in range (0,number_of_compounds):
        SMILES=cid[i].isomeric_smiles
        SMILES_all.append(str(SMILES))
    result_smiles.config(text='smiles: '+SMILES_all[0])


def CID_to_name(cid):
    names_all=[]
    synonyms_all=[]
    number_of_compounds=len(cid)
    for i in range (0,number_of_compounds):
        name=cid[i].iupac_name
        #synonym=cid[i].synonyms
        names_all.append(str(name))
        #synonyms_all.append(str(synonym))
    #result_synonyms.config(text='synonym: '+synonyms_all[0])
    result_name.config(text='name: '+names_all[0])
   

root = Tk()
label = Label(root,text='give CAS number/name/SMILES')
entry = Entry(root)

result0 = Label(root,text="")
#result_synonyms=Label(root,text="synonym:")
result_name= Label(root,text="name: ")
result_cas= Label(root,text="cas: ")
result_smiles= Label(root,text="smiles: ")

button=Button(text='Send',state='disabled',command=lambda:name_to_CID(entry))
entry.bind('<KeyRelease>',onKey)


label.pack()
entry.pack()
button.pack()
result0.pack()
#result_synonyms.pack()
result_name.pack()
result_cas.pack()
result_smiles.pack()

root.geometry("%dx%d%+d%+d" % (300,150,100,100))

root.mainloop()
