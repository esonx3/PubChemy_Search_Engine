import cPickle as pickle
#CAS_DB
#contains needed functions to handle the local CAS db


class CAS_DB:

    CAS_DB_L = {}#Global Database

    def __init__(self):
        CAS_DB.CAS_DB_L = self.Loade_CAS_DB()

    #loade the CAS database into the Global Variable CAS_DB
    #Use this function only once
    #out: loaded db if success, None if fails
    def Loade_CAS_DB(self):
        try:
            return pickle.load(open( "CAS_Cid.txt", "rb" ))
        except:
            return None

    #Prints the values in the CAS key db
    def Print_CAS_DB(self):
        con = 0
        for keys,values in CAS_DB.CAS_DB_L.items():
            con += 1
            print "Key(CID):" , keys," Value(CAS): ",values
        print "total ", con,"items found"

    #returns an list of found CID's that contains the CAS value
    #in: CAS = CAS as an string
    #in(optional): EndAtFirst = True to end on first match (faster)
    #out:list containing found CID's
    def Find_CID_BY_CAS(self,CAS,EndAtFirst=False):
        found_Key = list()
        for keys,values in CAS_DB.CAS_DB_L.items():
            for obj in values:
                if obj == CAS:
                    found_Key.append(keys)
                    if EndAtFirst:
                        return found_Key
        return found_Key

    #takes an CID and return its CAS as an string if it exists, if it don't return None
    #in: CID as an string or int
    #out: CAS as string or None
    def Find_CAS_BY_CID(self,CID):
        try:
            return CAS_DB.CAS_DB_L[str(CID)]
        except:
            return None
