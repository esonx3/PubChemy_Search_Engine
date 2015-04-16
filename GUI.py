from Tkinter import *
from tkFileDialog import askopenfilename
import data_fetching_class

from PIL import Image, ImageTk


import png
from pubchempy import download
def Creat_Button(topbar,img2):
    f1 = Frame(topbar, height=24, width=24)
    f1.pack_propagate(0)  # don't shrink
    f1.pack(side=LEFT)
    b1 = Button(f1, image=img2)
    b1.pack(fill=BOTH, expand=1)
    return b1

def onKey(event):
    #B.config(state='normal')
    print ("lol")

def get_last_key(event):
    if event == "1":
        print "knapp 1"
        return 1
    elif event == "2":
        print "knapp 2"
        return 2
    elif event == "3":
        print "knapp " + event
        return 3
    else:                       # remove the old text from the "enter window"
        print "enterkey..."
        return 0
def GetType():
    global var2
    print "selected: ", var2.get()
    return var2.get()

def search(event):
    global C
    global B
    global img5
    global separator2
    """
    :param event:
    :return:
    """
    #var_win_text = get_compounds(separator2.get(), 'name')
    #C.insert('1.0', var_win_text)
    print "search", event
    C.insert('1.0', "\n")
    if B.cget("state"):
        print B.cget("state"), "E.get"
    else:
        print "Disabled!"
    if get_last_key(event) == 0:
        type = GetType()
        obj = None
        error = False
        if type == "Name":
            try:
                obj = data_fetching_class.Chemical(name=separator2.get())
            except:
                print("Wrong formate, not Name")
                C.insert('1.0', "\n\n WARNING!: something went wrong, probably not an NAME entered\n\n")
                error = True
        elif type == "Smiley":
            try:
                obj = data_fetching_class.Chemical(smiles=separator2.get())
            except:
                print("Wrong formate, not Smily")
                C.insert('1.0', "\n\n WARNING!: something went wrong, probably not a Smily entered\n\n")
                error = True
        else:
            try:
                obj = data_fetching_class.Chemical(cas=separator2.get())
            except:
                print("Wrong formate, not CAS")
                C.insert('1.0', "\n\n WARNING!: something went wrong, probably not a CAS entered\n\n")
                error = True
        if not error:
            got_image = False
            try:
                try:
                    imgName = str(obj.CID_to_name()[0])
                except:
                    imgName = str(obj.CID_to_name())
                got_image = DownloadeImage(imgName)
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

def DownloadeImage(Name,type="name"):
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
    name = askopenfilename()

def save_file():
    pass

def go_name(B,C):
    B.config(text='Loading...')
    C.config(bg='grey')

def hello():
    print "hello!"

def search_log():
    about()

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

img2 = PhotoImage(file="firefox_icon.gif")
img5 = PhotoImage(file="firefox_icon.gif")

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


#TODO need to be redone later on...
#for g in range(1,3):

#knappar....
#img2 = PhotoImage(file="firefox_icon.gif")
#for n in range(0,3):
button = Creat_Button(topbar,img2)
#print str(n+1)
button.bind('<Button-1>', lambda(e): search(str(1)))
button1 = Creat_Button(topbar,img2)
button1.bind('<Button-1>', lambda(e): search(str(2)))
button2 = Creat_Button(topbar,img2)
button2.bind('<Button-1>', lambda(e): search(str(3)))

#button_object = CreateButton(topbar)
#button = button_object.small("1")
#button.bind('<Button-1>', lambda(e): search(C,B,separator2))

#bind hiden button
B.bind('<Button-1>', search)



#create OptionMenu
var2 = StringVar(root)
var2.set("Name") # initial value
separator3 = OptionMenu(topbar, var2, "Name", "Smiley", "CAS")
separator3.pack(fill=X, padx=5, pady=5)


separator2.bind('<Return>',search)
separator2.bind('<KeyRelease>',onKey) #Does nothing? reacting on key release

# create a toplevel menu
menubar = Menu(root)
# create pulldown menus, and add them to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file)  # change command to "read file"
filemenu.add_command(label="Save", command=save_file)  # change command to "save file"
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