#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *
from pubchempy import *
import cas_db

CAS_BDTABASE = cas_db.CAS_DB()


class Chemical:
    def __init__(self,name='',cas='',smiles=''):
        self.name=name
        self.cas=cas
        self.smiles=smiles
        self.CID=[]
        self.name_list=[]
        self.cas_list=[]
        self.smiles_list=[]
        if len(name)!=0:
            self.CID=self.name_to_CID(name)
        elif len(cas)!=0:
            self.CID=self.cas_to_CID(cas)
        elif len(smiles)!=0:
            self.CID=self.smiles_to_CID(smiles)
        self.name_list_print=''
        self.smiles_list_print=''
        self.cas_list_print=''

# gets CID number for a given name and summons functions getting all names, SMILES and a CAS number
    def name_to_CID(self,name):
        try:
            self.CID=get_compounds(self.name,'name')
            self.CID_to_name()
            self.CID_to_smiles()
            self.CID_to_CAS()
            return self.CID
        except:
            return self.CID

# gets CID number for a given SMILES and summons functions getting all names, SMILES and a CAS number
    def smiles_to_CID(self,smiles):
        try:
            self.CID=get_compounds(smiles,'smiles')
            self.CID_to_name()
            self.CID_to_smiles()
            self.CID_to_CAS()
            return self.CID
        except:
            return self.CID

# gets CID number for a given CAS number and summons functions getting all names, SMILES and a CAS number
    def cas_to_CID(self,cas):
        global CAS_BDTABASE
        try:
            self.CID = CAS_BDTABASE.Find_CID_BY_CAS(self.cas,True)
            self.CID=get_compounds(self.CID,'cid')
            self.CID_to_name()
            self.CID_to_smiles()
            self.CID_to_CAS()
            return self.CID
        except:
            return self.CID

# gets CAS number from CID number
    def CID_to_CAS(self):
        try:
            self.cas_list = CAS_BDTABASE.Find_CAS_BY_CID(self.CID[0].cid)
            print ("Cid hittades")
            print str(self.cas_list)
        except:
            print "No cid found.."
        return self.cas_list

# gets SMILES from CID number
    def CID_to_smiles(self):
        number_of_compounds=len(self.CID)
        for i in range (0,number_of_compounds):
            SMILES=self.CID[i].isomeric_smiles
            self.smiles_list.append(SMILES)
        return self.smiles_list

# gets names from CID number
    def CID_to_name(self):
        number_of_compounds=len(self.CID)
        for i in range (0,number_of_compounds):
            name=self.CID[i].iupac_name
            self.name_list.append(str(name))
        return self.name_list


    def __getitem__(self,key):
        if key =='name':
            return self.name
        elif key=='cas':
            return self.cas
        elif key=='smiles':
            return self.smiles
        elif key=='CID':
            return self.CID
        elif key=='name_list':
            return self.name_list
        elif key=='cas_list':
            return self.cas_list
        elif key=='name_list_print':
            if len(self.name_list) > 1:
                for nam in self.name_list:
                   self.name_list_print += nam + "\n"
            else:
                self.name_list_print = str(self.name_list[0])
            return self.name_list_print
        elif key=='smiles_list_print':
            if len(self.smiles_list) > 1:
                for smi in self.smiles_list:
                   self.smiles_list_print += smi + "\n"
            else:
                self.smiles_list_print = self.smiles_list[0]
            return self.smiles_list_print
        elif key=='smiles_list':
            return self.smiles_list
        else:
            return ''


    def __str__(self):
        return '\n\nThe inputs are: \n name: %(name)s ' \
               '\n cas number: %(cas)s ' \
               '\n SMILES: %(smiles)s' \
               '\n CID: %(CID)s ' \
               '\n name list: %(name_list)s' \
               '\n smiles list: %(smiles_list)s' \
               '\n cas list: %(cas_list)s' \
               '\n name new: %(name_list_print)s' % self

    def download_image(self):
        try:
            download('PNG', 'img/img.png', self.name_list[0],"name",overwrite=True)
            print "empty name list: " + str(self.name_list) + " end of empty list"
            return True
        except:
            return False
