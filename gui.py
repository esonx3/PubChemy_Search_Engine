# Application for PubChemy

from Tkinter import *
from tkFileDialog import askopenfilename
import data_fetching_class
import cPickle as pickle
from PIL_LIB import Image, ImageTk
from pubchempy import download


def create_button(topbar,img2):
    f1 = Frame(topbar, height=28, width=120)
    f1.pack_propagate(0)  # don't shrink
    f1.pack(side=LEFT)
    b1 = Button(f1, image=img2)
    b1.pack(fill=BOTH, expand=1)
    return b1


def on_key(event):
    pass


def get_last_key(event):
    if event == "1":
        print "knapp 1"
        return 1
    elif event == "2":
        print "knapp 2"
        return 2
    elif event == "3":
        print "knapp 3"
        return 3
    else:                       # remove the old text from the "enter window"
        print "enterkey..."
        return 0


def get_type():
    global var2
    print "selected: ", var2.get()
    return var2.get()


def search_array(array,logg=False):
    global Save_File
    global C
    global img5
    max = len(array)
    lengd = max
    first = True
    for target in array:
        type = get_type()
        action = action_by_type(type,target)
        error = action[0]
        obj = action[1]
        if first:
            first = False
            got_image = False
            try:
                try:
                    imgName = str(obj.CID_to_name()[0])
                except:
                    imgName = str(obj.CID_to_name())
                got_image = download_image(imgName)
            except:
                print("failed in getting a name..")
            if got_image:
                print("Got Image")
                #try:
                image = Image.open("img.png")
                C.insert('1.0', "\n\n Name of image: "+ str(obj.CID_to_name()[0]))
                img5 = ImageTk.PhotoImage(image)
                C.image_create('1.0', image=img5)
                #except:
                #   pass
        if logg:
            save_to_log(str(target))#save the search-term
        if not error:
            try:
                Name = str(obj.CID_to_name()[0])
            except:
                Name = str(obj.CID_to_name())
            try:
                smile = str(obj.CID_to_smiles()[0])
            except:
                smile = str(obj.CID_to_smiles())
            try:
                CAS = obj.CID_to_CAS()
                try:
                    tmp = ""
                    for t in CAS:
                        tmp += str(t) + " , "
                    CAS = tmp
                except:
                    CAS = str(CAS)
            except:
               CAS = "not found"
            SaveString = "\nName: " + Name + " Smile: " + smile + " CAS: " + CAS
            C.insert('1.0', "\nItem: "+str(lengd) + "/" + str(max) + ":" + SaveString + "\n")
            print SaveString
            f = open(Save_File, "a")
            f.write(SaveString)
            f.close()
            lengd -= 1
    C.insert('1.0',"\n")
    return True


def action_by_type(type,Data):
    obj = None
    error = False
    if type == "Name":
        try:
            obj = data_fetching_class.Chemical(name=Data)
        except:
            print("Wrong formate, not Name")
            C.insert('1.0', "\n\n WARNING!: something went wrong, probably not an NAME entered\n\n")
            error = True
    elif type == "Smiley":
        try:
            obj = data_fetching_class.Chemical(smiles=Data)
        except:
            print("Wrong formate, not Smily")
            C.insert('1.0', "\n\n WARNING!: something went wrong, probably not a Smily entered\n\n")
            error = True
    else:
        try:
            obj = data_fetching_class.Chemical(cas=Data)
        except:
            print("Wrong formate, not CAS")
            C.insert('1.0', "\n\n WARNING!: something went wrong, probably not a CAS entered\n\n")
            error = True
    print "action by type return: ", [error,obj]
    return [error,obj]


def search(event):
    global C
    global B
    global img5
    global separator2
    Data = separator2.get()
    #var_win_text = get_compounds(separator2.get(), 'name')
    #C.insert('1.0', var_win_text)
    #print "search", event
    #C.insert('1.0', "\n")
    num = get_last_key(event)
    if num == 0:
        type = get_type()
        action = action_by_type(type,Data)
        error = action[0]
        obj = action[1]
        save_to_log(Data)#save the search-term
        if not error:
            got_image = False
            try:
                try:
                    imgName = str(obj.CID_to_name()[0])
                except:
                    imgName = str(obj.CID_to_name())
                got_image = download_image(imgName)
            except:
                print("failed in getting a name..")
            #print to output window
            #print '\nAll found names for the input chemical are: \n' + obj['name_list_print']
            try:
                C.insert('1.0', "\n found object(s): "+str(obj['name_list_print']))
            except:
                print("error in data fetching")
                C.insert('1.0', "\n\n WARNING!: something went wrong, probably an invalid value entered\n\n")
            separator2.delete(0, END)
            if got_image:
                try:
                    image = Image.open("img.png")
                    C.insert('1.0', "\n\n Name of image: "+ str(obj.CID_to_name()[0]))
                    img5 = ImageTk.PhotoImage(image)
                    C.image_create('1.0', image=img5)
                except:
                    pass
    elif num == 1:
        open_file()
    elif num == 2:
        save_file()
    else:
        pass
    if B.cget("state"):
        print B.cget("state"), "E.get"
    else:
        print "Disabled!"


def download_image(Name,type="name"):
    print("data fetching goten,",Name)
    try:
        download('PNG', 'img.png', Name,type,overwrite=True)
        return True
    except:
        return False


def about():
    top = Toplevel()
    top.title("Python PubChem App")
    msg = Message(top, text="PubChem Client")
    msg.pack()

    button = Button(top, text="Ok", command=top.destroy)
    button.pack()


def open_file():
    global Open_File
    global Save_File
    global C
    if Save_File != None:
        Open_File = askopenfilename(filetypes=[("Text files","*.txt")])
        print "selected file:" , Open_File
        word_array = read_file()
        status = search_array(word_array,logg=True)
        if status:
            C.insert('1.0', "\nDONE!\nSave data to:\n" + str(Save_File))
    else:
        print "Save file not selected"
        C.insert('1.0', "\nSave file not selected!\n")


def save_file():
    global Save_File
    Save_File = askopenfilename(filetypes=[("Text files","*.txt")])
    print "selected file:" , Save_File


def go_name(B,C):
    B.config(text='Loading...')
    C.config(bg='grey')


def read_file():
    global Open_File
    f = open(Open_File, 'r+')
    Content = f.read()
    StringArray = Content.splitlines(False)
    print StringArray
    f.close()
    return StringArray


def hello():
    print "hello!"


def save_to_log(word):
    try:
        logg = pickle.load(open( "Logg.txt", "rb" ))
    except:
        logg = list()
    if len(logg) > 50:
        logg.pop(0)
    logg.append(word)
    pickle.dump(logg,open( "Logg.txt", "wb" ))


def search_log():
    global C
    try:
        logg = pickle.load(open( "Logg.txt", "rb" ))
    except:
        logg = ["Empty"]
    C.insert('1.0', "\n==============Search Logg Start=================)")
    for obj in logg:
        C.insert('1.0', "\n" + str(obj))
    C.insert('1.0', "\n===============Search Logg End==================)")
    #about()

#file to open
Open_File = None
#File to save in
Save_File = None


#def Gui_Start():
root = Tk()
topbar = Frame(height=300)
topbar.pack(fill=X)
tb = topbar

# Create 2:nd frame
frame = Frame()
frame.pack(fill=X)
#creat an scrollbar to the frame
scrollbar = Scrollbar(frame)

img2 = PhotoImage(file="img/icon_loadfile.gif")
img5 = PhotoImage(file="img/icon_loadfile.gif")

#text area for output
C = Text(frame, bg="white", wrap=WORD, yscrollcommand=scrollbar.set)
#C.insert(INSERT, "\n\nhello world")#hello world...
#scrollbar till outpot text
scrollbar.config(command=C.yview)
scrollbar.pack(side=RIGHT,  fill=Y)
C.config(yscrollcommand=scrollbar.set)
C.pack(side="left", fill=X, expand=True)

#creat buttons

#hiden button, (activated by enter key)
B = Button(topbar,state='disabled',command=lambda:go_name(B,C),text="GO!",fg="blue",bg="red",width=5)

# Entry widget
separator2 = Entry(relief=SUNKEN)
separator2.pack(fill=X, padx=5, pady=5)
separator2.focus()


#knappar....
#img2 = PhotoImage(file="firefox_icon.gif")
save_img = PhotoImage(file="img/icon_savefile.gif")
Load_img = PhotoImage(file="img/icon_loadfile.gif")
img2 = PhotoImage(file="img/icon_loadfile.gif")
button = create_button(topbar,Load_img)
button.bind('<Button-1>', lambda(e): search(str(1)))
button1 = create_button(topbar,save_img)
button1.bind('<Button-1>', lambda(e): search(str(2)))


#bind hiden button
B.bind('<Button-1>', search)

#create OptionMenu
var2 = StringVar(root)
var2.set("Name") # initial value
separator3 = OptionMenu(topbar, var2, "Name", "Smiley", "CAS")
separator3.pack(fill=X, padx=5, pady=5)


separator2.bind('<Return>',search)
separator2.bind('<KeyRelease>',on_key) #Does nothing? reacting on key release

# create a toplevel menu
menubar = Menu(root)
# create pulldown menus, and add them to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open file", command=open_file)  # change command to "read file"
filemenu.add_command(label="Select save file", command=save_file)  # change command to "save file"
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

historymenu = Menu(menubar, tearoff=0)
historymenu.add_command(label="Search log", command=search_log)
historymenu.add_command(label="Random function", command=hello)
menubar.add_cascade(label="History", menu=historymenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)  #change command to print instructions in window
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)
mainloop()
#Gui_Start()
