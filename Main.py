#Main file
from pubchempy import *
import CAS_DB

CAS_BDTABASE = CAS_DB.CAS_DB()#creat an global database object

#pubchempy doc: http://pubchempy.readthedocs.org/en/latest/

#Retrieve Compound record for specified CID
#in: CID
#out: Compound record
def GetCompound(id):
    comp = Compound.from_cid(id)
    return comp.isomeric_smiles

#takes an cas and return its cid
#in: CAS
#out: Cid
#TODO remove later on, test function only
def Test_CAS_TO_CID(CAS):
    global CAS_BDTABASE
    cid_list = CAS_BDTABASE.Find_CID_BY_CAS(CAS,True)
    return int(cid_list[0])


#print given value or values, most likely not needed
#in: item to print
# TODO Remove this if it ain't needed
def PrintValue(val):
    try:
        for obj in val:
            print "item",val.index(obj)+1,":",obj
    except:
        print "one item:",val

#Test function, remove later on
# TODO Remove this later on
def Test():
    CID_list = [1423,1451,1321,25,962]
    forms = list()
    for obj in CID_list:
        comp = GetCompound(obj)
        forms.append(comp)
    return forms

#print the returned values from the test function
PrintValue(Test())

#test the cas to cid function


print "enter cas key '7732-18-5' (water)"
cas_key = "7732-18-5"
print "got smile: "
print GetCompound(Test_CAS_TO_CID(cas_key))
print "enter cas key '7782-99-2' (Sulfurous)"
cas_key = "7782-99-2"
print "got smile: "
print GetCompound(Test_CAS_TO_CID(cas_key))