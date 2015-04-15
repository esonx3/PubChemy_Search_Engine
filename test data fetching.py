#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *
from pubchempy import *
import CAS_DB

CAS_BDTABASE = CAS_DB.CAS_DB()



class Chemical:

    def __init__(self,name='',cas='',smiles=''):
        self.name=name
        self.cas=cas
        self.smiles=smiles
        self.CID=[]
        self.name_list=[]
        self.cas_list=[]
        self.smiles_list=[]

    def name_to_CID(self,name):
        #result0.config(text="")
        #button.config(text='Loading...')
        #self.name=str(self.name.get())
        try:
            self.CID=get_compounds(self.name,'name')
            #CID_to_name(cid)
            #CID_to_smiles(cid)
            return self.CID
        except:
            #result0.config(text="Your compound most probably doesn't exist")
            return self.CID


    def smiles_to_CID(self,smiles):
        #result0.config(text="")
        self.smiles=str(smiles.get())
        try:
            self.CID=get_compounds(smiles,'smiles')
            #print "CID: ", cid
            #CID_to_name(cid)
            #CID_to_smiles(cid)
            return self.CID
        except:
            #result0.config(text="Your compound most probably doesn't exist")
            return self.CID

    #global CAS_BDTABASE
    #cas=str(raw_input('give a cas: '))
    ##cid=get_compounds(smiles,'smiles')
    #cid = CAS_BDTABASE.Find_CID_BY_CAS(cas,True)
    #print 'cid: ' + str(cid)


    def cas_to_CID(self,cas):
        global CAS_BDTABASE
        #sometext=str(CAS.get())
        #print "CAS: ", sometext
        try:
            self.CID = CAS_BDTABASE.Find_CID_BY_CAS(self.cas,True)
            self.CID=get_compounds(self.CID,'cid')
            return self.CID
        except:
            #result0.config(text="Your compound most probably doesn't exist" \
            #               "or is missing in the local cas database")
            return self.CID
        #cid = ("Compound("+cid[0]+")",)
        #print "CID:" , cid[0]
    #    return int(cid[0])
        #CID_to_name(cid)
        #CID_to_smiles(cid)

    def send(self,name,cas,smiles):
        if len(name)!=0:
            self.CID=self.name_to_CID(name)
        elif len(cas)!=0:
            self.CID=self.cas_to_CID(cas)
        elif len(smiles)!=0:
            self.CID=self.smiles_to_CID(smiles)
        return self.CID

    def get_all(self,CID):
        self.CID_to_smiles(self.CID)
        self.CID_to_name(self.CID)

    def CID_to_smiles(self,CID):
        #SMILES_all=[]
        number_of_compounds=len(self.CID)
        for i in range (0,number_of_compounds):
            SMILES=self.CID[i].isomeric_smiles
            self.smiles_list.append(SMILES)
        #result_smiles.config(text='smiles: '+SMILES_all[0])
        #self.smiles_list=SMILES_all[0]
        return self.smiles_list

    def CID_to_name(self,CID):
        #names_all=[]
        number_of_compounds=len(self.CID)
        for i in range (0,number_of_compounds):
            name=self.CID[i].iupac_name
            self.name_list.append(str(name))
        #result_name.config(text='name: '+name[0])
        #self.name=nameiupac_all[0]
        return self.name_list

        ##print All elements in a nice list
    def print_lists(self,name_list,cas_list,smiles_list):
        if len(self.name_list) > 1:
            nameprint = ""
            for nam in self.name_list:
                nameprint += nam + " ,"
            else:
                nameprint = self.name_list[0]
        #result_name.config(text='name: '+nameprint)
        if len(self.cas_list) > 1:
            casprint = ""
            for cas in self.cas_list:
                casprint += cas + " ,"
            else:
                casprint = self.cas_list[0]
        if len(self.smiles_list) > 1:
            smilesprint = ""
            for smi in self.smiles_list:
                smilesprint += smi + " ,"
            else:
                smilesprint = self.smiles_list[0]
        print 'name: '+ nameprint
        print 'cas: ' + casprint
        print 'smiles: ' + smilesprint

#    def __getitem__(self,key):
#        if key =='name':
#            return self.name_list[0]
#        elif key=='cas':
#            return self.cas_list[0]
#        elif key=='smiles':
#            return self.smiles_list[0]
#        else:
#            return ''


#    def __str__(self):
#        return 'This compound is named: %(name)s, has cas number: %(cas)s ' \
#               'and SMILES: %(smiles)s' % self

name='glucose'
cas=''
smiles=''

kemikalie=Chemical('glucose')
print 'kemikalie nu: ' + str(kemikalie)

if len(name)!=0:
    CID=kemikalie.name_to_CID(name)
    print CID
    smiles=kemikalie.CID_to_smiles(CID)
    print 'smiles: ' + str(smiles)
    all=kemikalie.get_all(CID)
    print all
elif len(cas)!=0:
    CID=kemikalie.cas_to_CID(cas)
elif len(smiles)!=0:
    CID=kemikalie.smiles_to_CID(smiles)


#kemikalie.get_all()
