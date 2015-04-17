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

    def name_to_CID(self,name):
        try:
            self.CID=get_compounds(self.name,'name')
            self.CID_to_name()
            self.CID_to_smiles()
            return self.CID
        except:
            return self.CID


    def smiles_to_CID(self,smiles):
        try:
            self.CID=get_compounds(smiles,'smiles')
            self.CID_to_name()
            self.CID_to_smiles()
            return self.CID
        except:
            return self.CID

    #global CAS_BDTABASE
    #cas=str(raw_input('give a cas: '))
    ##cid=get_compounds(smiles,'smiles')
    #cid = CAS_BDTABASE.Find_CID_BY_CAS(cas,True)
    #print 'cid: ' + str(cid)

    def CID_to_CAS(self):
        #if self.cas == '':
        try:
            self.cas = CAS_BDTABASE.Find_CAS_BY_CID(self.CID[0].cid)
        except:
            print "No cid found.."
        return self.cas
        #else:
         #   return self.cas
    def cas_to_CID(self,cas):
        global CAS_BDTABASE
        try:
            self.CID = CAS_BDTABASE.Find_CID_BY_CAS(self.cas,True)
            self.CID=get_compounds(self.CID,'cid')
            self.CID_to_name()
            self.CID_to_smiles()
            return self.CID
        except:
            return self.CID

    def get_all(self):
        smile = self.CID_to_smiles()
        name = self.CID_to_name()
        return [smile, name]

    def CID_to_smiles(self):
        number_of_compounds=len(self.CID)
        for i in range (0,number_of_compounds):
            SMILES=self.CID[i].isomeric_smiles
            self.smiles_list.append(SMILES)
        return self.smiles_list

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
        elif key=='name_list_print':
            if len(self.name_list) > 1:
                for nam in self.name_list:
                   self.name_list_print += nam + "\n"
            else:
                self.name_list_print = self.name_list[0]
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
               '\n name new: %(name_list_print)s' % self


# TEST

#kemikalie=Chemical(name='glucose')
#kemikalie2=Chemical(smiles='CCCCC')
#kemikalie3=Chemical(cas='7732-18-5')

#print kemikalie
#print 'The input name of a chemical is: ' + kemikalie['name']
#print '\nAll found names for the input chemical are: \n' + kemikalie['name_list_print']

#print kemikalie2
#print 'The input name of a chemical is: ' + kemikalie2['name']
#print 'The input smiles of a chemical is: ' + kemikalie2['smiles']
#print '\nAll found names for the input chemical are: \n' + kemikalie2['name_list_print'] + '\n'

#print kemikalie3
#print 'The input name of a chemical is: ' + kemikalie3['name']
#print 'The input smiles of a chemical is: ' + kemikalie3['smiles']
#print 'The input cas number of a chemical is: ' + kemikalie3['cas']
#print '\nAll found names for the input chemical are: \n' + kemikalie3['name_list_print']
