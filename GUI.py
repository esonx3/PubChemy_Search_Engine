
from Tkinter import *

root = Tk()

#testar lite olika funktioner för användar fönstret


# create a frame
frame = Frame()
frame.pack()

v = StringVar()
Entry(frame,textvariable=v).grid(row=3, column=1)
Entry(frame,textvariable=v).grid(row=3, column=0)



#create button
B1=Button(frame,text="basic",fg="red",bg="blue",width=12)
B1.pack(side=LEFT, padx=10)
B2=Button(frame,text="basic",fg="blue",bg="red",width=12)
B2.pack(side=LEFT, padx=10)

B1.grid(row=1, column=0)
B2.grid(row=2, column=1)

B3=Button(frame,text="basic",fg="Green",bg="Black",width=12)
B3.pack(side=LEFT, padx=10)
B4=Button(frame,text="basic",fg="Green",bg="Black",width=12)
B4.pack(side=RIGHT, padx=10)

B3.grid(row=1, column=1)
B4.grid(row=2, column=0)

Label(frame, text="This is a label").grid(row=0,column=0, sticky=W)
Label(frame, text="Another lable").grid(row=0, column=1, sticky=W)

#herp di derp funktion
C=Canvas(frame,width=300, height=100)
C.grid(row=4, column=0,)
C.create_line(0, 100, 100, 100)


mainloop()