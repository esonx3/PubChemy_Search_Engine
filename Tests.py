import urllib
import cPickle as pickle
print "started"

def DownloadDB(start,end):
    current = start
    #ListOfFoundObjects = list()
    #dicti = {}
    dicti = pickle.load(open( "CAS_Cid.txt", "rb" ))
    while current < end:
        try:
            print "Item: ", current
            Object = list()
            link = "https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/" + str(current) + "/JSONP/?callback=jQuery210016954221896634825_1427811263840"
            sock = urllib.urlopen(link)
            htmlSource = sock.read()
            sock.close()
            htmlAsString = str(htmlSource)
            ins = htmlAsString.find('"Name": "CAS",')
            continioue = True
            strofcount = 0
            polcount = 0
            mincount = 0
            line = ""
            insmen = ins + 500
            while continioue:
                if htmlAsString[ins] != ' ':
                    print htmlAsString[ins]
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
                        break;
                ins += 1
                if ins > insmen:
                    break;
            if line[len(line)-1] == '"':
                line = line[:len(line)-1]
            #ListOfFoundObjects.append((line,current))
            dicti[str(current)] = line
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

DownloadDB(1,5000)
#openandprint()