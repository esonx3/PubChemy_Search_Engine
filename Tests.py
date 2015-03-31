import urllib
import cPickle as pickle
print "started"

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
                    if line[len(line)-1] == '"':
                        line = line[:len(line)-1]
                    tempList.append(line)
                #ListOfFoundObjects.append((line,current))
                dicti[str(current)] = tempList
                current += 1
            except:
                print "logic error in loops, or index out of bounds...."
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
def openandprint():
    dicti = pickle.load(open( "CAS_Cid.txt", "rb" ))
    for keys,values in dicti.items():
        print keys,":",values

DownloadDB(1,5)
openandprint()