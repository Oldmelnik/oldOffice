import os, pygame
from tkinter.filedialog import askdirectory
from tkinter import *
from mutagen.id3 import ID3


root = Tk()

root.minsize(250,350)
root.title('OlD Music Player')
root.configure(background='#4b6584')


listofsongs = []
#realnames = []

v = StringVar()
songlabel = Label(root,textvariable=v,width=35,bg='#45aaf2',font="Arial")

index = 0
coun = 0

if os.path.exists("C:/oldof/volf.tx"):
	volf = open("volf.tx",'r')
	vol = volf.read()
	vol = float(vol)
	volf.close()
	print(vol)
else:
	#vol = 1.0
	#vol = float(vol)
	#os.makedirs("C:/oldof/vol.tx")
	volf = open("volf.tx","w")
	volf.write(str(vol))
	volf.close()


if vol < 0:
	vol = 0

if vol > 1.0:
	vol = 1.0


while pygame.mixer.music.get_busy == False:
	nextsong()
	
print("ITS WORKING!")

#sselect = index(listofsongs.curselection())


#////////Buttons events/////////

def nextsong(event):
	global index
	index += 1

	if index > coun-1:
		index = 0

	if index < 0:
		index = 0


	pygame.mixer.music.load(listofsongs[index])
	pygame.mixer.music.play()
	#update(label)
	
	v.set(listofsongs[index])
	print('track num ',index)
	#pygame.mixer.music.queue[index-1].stop
	#pygame.mixer.music.queue[index].play()




def prevsong(event):
	global index
	index -= 1

	if index > coun:
		index = 0

	if index < 0:
		index = coun-1

	pygame.mixer.music.load(listofsongs[index])
	pygame.mixer.music.play()
	#update(label)
	v.set(listofsongs[index])
	print('track num ',index)

def stopsong(event):
	pygame.mixer.music.pause()
	index = 0
	print('paused')

def playsong(event):
	pygame.mixer.music.unpause()
	#update(label)
	v.set(listofsongs[index])
	print("playing now")

def curetsel(event):
	index= int(listofsongs.curselection()[0])
	playsong(index)
	print(index)



pln=True

def domsplay(event):
	pygame.mixer.music.get_busy() 
	if pygame.mixer.music.get_busy() == False:
		nextsong()
	while pygame.mixer.music.get_busy == False:
		nextsong()



def volup(event):
	global vol
	vol = float(vol)
	vol +=0.1

	#vol = (vol)
	volf = open("volf.tx",'w')
	volf.write(str(vol))
	print(vol)
	volf.close()
	vol = float(vol)
	#volf.close()
	pygame.mixer.music.set_volume(vol)
	if vol < 0:
		vol = 0

	if vol > 1.0:
		vol = 1.0



	print("vol",pygame.mixer.music.get_volume())

def voldown(event):
	global vol
	vol = float(vol)
	vol -= 0.1

	#vol = (vol)
	volf = open("volf.tx",'w')
	volf.write(str(vol))
	volf.close()
	vol = float(vol)
	#volf.close()
	pygame.mixer.music.set_volume(vol)
	if vol < 0:
		vol = 0

	if vol > 1.0:
		vol = 1.0



	print("vol",pygame.mixer.music.get_volume())


#def udatelabel():
	#global index
	#global songname
	#v.set(listofsongs[index])
	#return songname



def directorychooser():

	directory = ("C:/oldof/muz")#askdirectory()
	os.chdir(directory)

	for files in os.listdir(directory):
		if files.endswith(".mp3"):

			realdir = os.path.realpath(files)
			#audio = ID3(realdir)
			#realnames.append(audio['TIT2'].text[0])

			listofsongs.append(files)


	pygame.mixer.init()
	pygame.mixer.music.load(listofsongs[0])
	pygame.mixer.music.play()
	pygame.mixer.music.set_volume(vol)
	#pygame.mixer.music.queue(index+1)
	print('get vol = ',pygame.mixer.music.get_volume())

directorychooser()

print("curent song ",index)

#//////////////////////////
label = Label(root,text="Playlist",bg='#d1d8e0',font="Arial")
label.pack()


listbox = Listbox(root,width=40,bg='#f5f6fa')
listbox.pack()


listofsongs.reverse()
#realnames.reverse()

for items in listofsongs:
	listbox.insert(0,items)

listofsongs.reverse()
#realnames.reverse()

#//////buttons////////////
nextbutton = Button(root,text = 'Next song',bg='#dcdde1',font="Arial")
nextbutton.pack()


previousbutton = Button(root,text = 'Prev song',bg='#dcdde1',font="Arial")
previousbutton.pack()



stopbutton = Button(root,text='Pause',bg='#dcdde1',font="Arial")
stopbutton.pack()

playbutton = Button(root,text=" Play ",bg='#dcdde1',font="Arial")
playbutton.pack()

volupbutton = Button(root,text="+",bg="#dcdde1",font="Arial")
volupbutton.pack()

voldownbutton = Button(root,text="--",bg="#dcdde1",font="Arial")
voldownbutton.pack()


#/////BInd button///////////
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
playbutton.bind('<Button-1>',playsong)
volupbutton.bind('<Button-1>',volup)
voldownbutton.bind('<Button-1>',voldown)



#///////////ButtonPlace/////////////
playbutton.place(x=127,y=250)
stopbutton.place(x=125,y=285)
nextbutton.place(x=185,y=250)
previousbutton.place(x=37,y=250)

volupbutton.place(x=10,y=0)
voldownbutton.place(x=10,y=35)



songlabel.pack()




for items in listofsongs:
	coun = coun+1

print('songs count  ',coun)

#labelss = Label(root, text = "Songs count -",textvariable=coun, bg ="#D4E6F1",width=25)
#labelss.pack()

v.set(listofsongs[index])


while pygame.mixer.music.get_busy == False:
	nextsong()

root.mainloop()