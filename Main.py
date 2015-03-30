#Main file

from pubchempy import *

#Test function, remove later on
# TODO Remove this later on
def TestFunction(id):
    comp = Compound.from_cid(id)
    return comp.isomeric_smiles

#print given value
def PrintValue(val):
    print val



PrintValue(TestFunction(1423))
