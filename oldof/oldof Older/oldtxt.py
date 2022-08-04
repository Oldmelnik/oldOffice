import sys
from tkinter import *
from tkinter.filedialog import *
import datetime

import subprocess

root=Tk("TxT")
root.minsize(600,400)
root.title("TxT")
root.configure(background='#4b6584')
print("RUNNING!!!")

if not os.path.exists("C:/oldof/noter/"):
    os.makedirs("C:/oldof/noter/")

fname = Text(root,width=25,height=1,font="Arial 10")
fname.grid()

text = Text(root,width=60,height=20.4,font="Arial 12")
text.grid()

#text.insert(1.0,voice.cmd)

if os.path.exists("C:/oldof/noter/temp.tx"):
	file = open("C:/oldof/noter/temp.tx","r")
	cmd = file.read()
	text.insert(1.0,cmd)
	#os.remove("C:/oldof/noter/temp.tx")

def saveas():
	global text
	if text.get("1.0").strip():

		t = text.get("1.0","end-1c")
		if fname.get("1.0").strip():
			ffname = fname.get("1.0","end-1c")
			savelocation = ("C:/oldof/noter/"+ffname.replace("/",""))
		else:
			namef=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
			savelocation = ("C:/oldof/noter/"+namef+".tx")

		file1=open(savelocation,"w+")
		file1.write(t)
		file1.close()
		print("Saved")
	else:
		print("EMPTY FILE")

def get_text(cmd):
	from voice import cmd
	global text
	text.delete(1.0,END)
	text.insert(1.0,voice.cmd)



def openf():
	global text
	openlocation = askopenfilename()
	file1=open(openlocation,"r")
	t = file1.read() 
	text.delete(1.0,END)
	text.insert(1.0,t)
	text

	fname.delete(1.0,END)
	fname.insert(1.0,openlocation.replace("C:/oldof/noter/",""))

	file1.close()
	print("opened")

def clrscr():
	global text
	text.delete(1.0,END)
	fname.delete(1.0,END)

def exitf():
	sys.exit("Bye - bye !")

clrbutton = Button(root,text="CLear",bg = "#b71540",font = "calibri 12",height = 3,width = 5, command=clrscr)
clrbutton.grid()
clrbutton.place(x=545,y=310)

sbutton = Button(root,text="Save",bg = "#60a3bc", font = "calibri 12",height = 3,width = 5,command=saveas)
sbutton.grid()
sbutton.place(x=545,y=20)

lbutton = Button(root,text="Open",bg = "#60a3bc", font="calibri 12",height = 3,width = 5, command=openf)
lbutton.grid()
lbutton.place(x=545,y=100)

exbutton = Button(root,text="Exit",bg = "#778beb", font="calibri 12",height = 3,width = 5, command=exitf)
exbutton.grid()
exbutton.place(x=545,y=200)

root.mainloop()