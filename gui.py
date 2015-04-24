# Application for PubChemy

from Tkinter import *
from tkFileDialog import askopenfilename
import data_fetching_class
import cPickle as pickle
from PIL_LIB import Image, ImageTk
#from pubchempy import download

#Function to create buttons with pictures
def create_button(topbar,img2):
    f1 = Frame(topbar, height=28, width=120)
    f1.pack_propagate(0)  # don't shrink
    f1.pack(side=LEFT)
    b1 = Button(f1, image=img2)
    b1.pack(fill=BOTH, expand=1)
    return b1

#what purpose does this have?
#def on_key(event):
#    pass

#Cant we remove this whole function after we are done? it only prints in Python window and returns same value as it get?
def get_last_key(event):
    if event == "1":
        return 1
    elif event == "2":
        return 2

    #event==3 is not going to occur so should be removed
    elif event == "3":
        return 3
    else:                       # remove the old text from the "enter window"
        return 0

#Determins the Type of search that is going to be preformed
def get_type():
    global Type_var
    return Type_var.get()

#Preforms a search, depending on Type. Saves the search to a logfile. And inserts the result on screen in GUI
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
                got_image=str(obj.download_image())

                if got_image:
                    print("Got Image")
                    image = Image.open("img/img.png")
                    C.insert('1.0', "\n\n Name of image: "+ str(obj.CID_to_name()[0]))
                    img5 = ImageTk.PhotoImage(image)
                    C.image_create('1.0', image=img5)
            except:
                pass
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
            #Testing print, shows SaveString in Python. Does nothing in GUI
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
            C.insert('1.0', "\n\n WARNING!: something went wrong, probably not an NAME entered\n\n")
            error = True
    elif type == "SMILES":
        try:
            obj = data_fetching_class.Chemical(smiles=Data)
        except:
            C.insert('1.0', "\n\n WARNING!: something went wrong, probably not a Smily entered\n\n")
            error = True
    else:
        try:
            obj = data_fetching_class.Chemical(cas=Data)
        except:
            C.insert('1.0', "\n\n WARNING!: something went wrong, probably not a CAS entered\n\n")
            error = True
    return [error,obj]


def search(event):
    global C
    global B
    global img5
    global separator2
    Data = separator2.get()
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
                got_image=str(obj.download_image())
            except:
                pass


            try:
                try:
                    C.insert('1.0', "\n found name(s): "+str(obj['name_list_print']))
                except:
                    C.insert('1.0', "\n Name is incorrect")

                try:
                    C.insert('1.0', "\n found SMILES(s): "+str(obj['smiles_list_print']))
                except:
                    C.insert('1.0', "\n SMILES is incorrect")

                try:
                    if str(obj['CID']) != "[]":
                        C.insert('1.0', "\n found CID(s): "+str(obj['CID']))
                    else:
                        C.insert('1.0', "\n Cas is possibly incorrect")
                except:
                    C.insert('1.0', "\n Cas is possibly incorrect")
            except:
                pass
            separator2.delete(0, END)
            if got_image:
                try:
                    image = Image.open("img/img.png")
                    C.insert('1.0', "\n\n Name of image: "+ str(obj.CID_to_name()[0]))
                    img5 = ImageTk.PhotoImage(image)
                    C.image_create('1.0', image=img5)
                    C.insert('1.0', "\n")
                except:
                    pass
    elif num == 1:
        open_file()
    elif num == 2:
        save_file()
    else:
        pass


def about():
    top = Toplevel()
    top.title("Python PubChem App")
    msg = Message(top, text="PubChem Client\nCreated by Tony, Alexander, Aleksandra and Markus\n\n Expect 3seconds per search term, so dont be a stupid fuck and search for to manny at a time!!!")
    msg.pack()

    button = Button(top, text="Ok", command=top.destroy)
    button.pack()


def open_file():
    global Open_File
    global Save_File
    global C
    if Save_File != None:
        Open_File = askopenfilename(filetypes=[("Text files","*.txt")])
        word_array = read_file()
        status = search_array(word_array,logg=True)
        if status:
            C.insert('1.0', "\nDONE!\nSave data to:\n" + str(Save_File))
    else:
        C.insert('1.0', "\nSave file not selected!\n")


def save_file():
    global Save_File
    temp = askopenfilename(filetypes=[("Text files","*.txt")])
    if len(temp) > 1:
        Save_File = temp


def go_name(B,C):
    B.config(text='Loading...')
    C.config(bg='grey')


def read_file():
    global Open_File
    f = open(Open_File, 'r+')
    Content = f.read()
    StringArray = Content.splitlines(False)
    f.close()
    return StringArray


def hello():
    global C
    import random
    rand=['Hello!','Surprise!','This is a random function!','Bored?',"I'm sick of it!"]
    C.insert('1.0',"\n"+random.choice(rand)+"\n"+"\n")


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
#creat a scrollbar to the frame
scrollbar = Scrollbar(frame)

img2 = PhotoImage(file="img/icon_loadfile.gif")
img5 = PhotoImage(file="img/icon_loadfile.gif")

#text area for output
C = Text(frame, bg="white", wrap=WORD, yscrollcommand=scrollbar.set)
#configure scrollbar
scrollbar.config(command=C.yview)
scrollbar.pack(side=RIGHT,  fill=Y)
C.config(yscrollcommand=scrollbar.set)
C.pack(side="left", fill=X, expand=True)

#---- Create buttons ----

#Hiden button, (activated by enter key)
B = Button(topbar,state='disabled',command=lambda:go_name(B,C),text="GO!",fg="blue",bg="red",width=5)
# Entry widget
separator2 = Entry(relief=SUNKEN)
separator2.pack(fill=X, padx=5, pady=5)
separator2.focus()
#Create load and save buttons
save_img = PhotoImage(file="img/icon_savefile.gif")
Load_img = PhotoImage(file="img/icon_loadfile.gif")
loadButton = create_button(topbar,Load_img)
#Binds commands to buttons
loadButton.bind('<Button-1>', lambda(e): search(str(1)))
saveButton = create_button(topbar,save_img)
saveButton.bind('<Button-1>', lambda(e): search(str(2)))
#Bind command to hiden button
B.bind('<Button-1>', search)

#create OptionMenu
Type_var = StringVar(root)
Type_var.set("Name") # initial value
separator3 = OptionMenu(topbar, Type_var, "Name", "SMILES", "CAS")
separator3.pack(fill=X, padx=5, pady=5)


separator2.bind('<Return>',search)
#vad ar syftet med den har raden kod??
#separator2.bind('<KeyRelease>',on_key) #Does nothing? reacting on key release

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
helpmenu.add_command(label="About", command=about)  #Adds command to print instructions in window
menubar.add_cascade(label="Help", menu=helpmenu)

C.insert('1.0',"\n\nExpect 3seconds per search term, so dont be a stupid fuck and search for to manny at a time!!!")
# display the menu
root.config(menu=menubar)
mainloop()
