import urllib
import cPickle as pickle
print "started"

#This function is used to update the local CAS to CID db
#It loades an page as an string, finds the needed values and updates the file CAS_Cid.txt


#WARNING!
#DON'T USE OR RUN THIS FUNCTION UNLESS YOU RLY KNOW WHAT U ARE DOING!

#TODO comment this sh1et


def DownloadDB(start,end):
    print "Updating values from ", start, "to ", end
    current = start
    #ListOfFoundObjects = list()
    #dicti = {}
    dicti = pickle.load(open( "CAS_Cid.txt", "rb" ))
    while current <= end:
        try:
            print "Updating valu: ", current
            Object = list()
            link = "https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/" + str(current) + "/JSONP/?callback=jQuery210016954221896634825_1427811263840"
            sock = urllib.urlopen(link)
            htmlSource = sock.read()
            sock.close()
            htmlAsString = str(htmlSource)
            continioue = False
            tempList = list()
            try:
                while continioue == False:
                    ins = htmlAsString.find('"Name": "CAS",')
                    continioue = True
                    strofcount = 0
                    polcount = 0
                    mincount = 0
                    line = ""
                    insmen = ins + 500
                    try:
                        while continioue:
                            if htmlAsString[ins] != ' ':
                                #print htmlAsString[ins]
                                if (strofcount == 7 and polcount == 2):
                                    line += htmlAsString[ins]
                                if htmlAsString[ins] == '"':
                                    strofcount += 1
                                elif htmlAsString[ins] == ':':
                                    polcount += 1
                                elif htmlAsString[ins] == '-':
                                    mincount += 1
                                Object.append(htmlAsString[ins])
                                if (strofcount == 8 and polcount == 2 and mincount == 2):
                                    continioue = False
                                    htmlAsString = htmlAsString[ins:]
                                    print "found CAS: ", line, "at cid: ", current
                                    break;
                            ins += 1
                            if ins > insmen:
                                break;
                    except:
                        print "logic error in loops, or index out of bounds....(stage 1)"
                        ins += 1
                    try:
                        if line[len(line)-1] == '"':
                            line = line[:len(line)-1]
                        tempList.append(line)
                    except:
                        print "missing an definition..."
                #ListOfFoundObjects.append((line,current))
                dicti[str(current)] = tempList
                current += 1
            except:
                print "logic error in loops, or index out of bounds....(stage 2)"
                current += 1
        except:
            print "WARNING! Object ",current, " passed!"
            current += 1
    #for keys,values in dicti.items():
    #    print keys,":",values
    print "Done!"
    #for obj in ListOfFoundObjects:
    #    print "CAS: ", obj[0], " CID: ", obj[1]
    pickle.dump(dicti,open( "CAS_Cid.txt", "wb" ))
#TODO comment here
def openandprint():
    dicti = pickle.load(open( "CAS_Cid.txt", "rb" ))
    con = 0
    for keys,values in dicti.items():
        con += 1
        print keys,":",values
    print "total ", con,"CAS cid's found!"
#TODO comment here
def Cleaner():
    dicti = pickle.load(open( "CAS_Cid.txt", "rb" ))
    for keys,values in dicti.items():
        try:
            if values[0] == 'RecordNumber' or values[0] == ' ' :
              del dicti[keys]
        except:
            pass
    pickle.dump(dicti,open( "CAS_Cid.txt", "wb" ))
#DownloadDB(3000,6000)
#Cleaner()
#print "Done!"
#openandprint()