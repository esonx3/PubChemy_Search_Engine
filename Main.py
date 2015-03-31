#Main file
from pubchempy import *

#pubchempy doc: http://pubchempy.readthedocs.org/en/latest/


#Retrieve Compound record for specified CID
#in: CID
#out: Compound record
def GetCompound(id):
    comp = Compound.from_cid(id)
    return comp.isomeric_smiles

#print given value or values, most likely not needed
#in: item to print
def PrintValue(val):
    try:
        for obj in val:
            print "item",val.index(obj)+1,":",obj
    except:
        print "one item:",val

#Test function, remove later on
# TODO Remove this later on
def Test():
    CID_list = [1423,1451,1321,25]
    forms = list()
    for obj in CID_list:
        comp = GetCompound(obj)
        forms.append(comp)
    return forms

#print the returned values from the test function
PrintValue(Test())


