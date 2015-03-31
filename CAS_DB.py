import cPickle as pickle
#CAS_DB
#contains needed functions to handle the local CAS db


CAS_DB = {}#Global Database

#loade the CAS database into the Global Variable CAS_DB
#Use this function only once
#out: True if sucess, False if fails
def Loade_CAS_DB():
    global CAS_DB
    try:
        CAS_DB = pickle.load(open( "CAS_Cid.txt", "rb" ))
        return True
    except:
        return False

#Prints the values in the CAS key db
def Print_CAS_DB():
    global CAS_DB
    con = 0
    for keys,values in CAS_DB.items():
        con += 1
        print "Key(CID):" , keys," Value(CAS): ",values
    print "total ", con,"items found"

#returns an list of found CID's that contains the CAS value
#in: CAS = CAS as an string
#in(optional): EndAtFirst = True to end on first match (faster)
#out:list containing found CID's
def Find_CID_BY_CAS(CAS,EndAtFirst=False):
    global CAS_DB
    found_Key = list()
    for keys,values in CAS_DB.items():
        for obj in values:
            if obj == CAS:
                found_Key.append(keys)
                if EndAtFirst:
                    return found_Key
    return found_Key

#takes an CID and return its CAS as an string if it exists, if it don't return None
#in: CID as an string or int
#out: CAS as string or None
def Find_CAS_BY_CID(CID):
    global CAS_DB
    try:
        return CAS_DB[str(CID)]
    except:
        return None