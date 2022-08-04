import os,sys
import time
import speech_recognition as sr
#import pyttsx3
import datetime
import win32com.client as wincl
import subprocess
import random
import pyautogui
import pygame
#import weather

pygame.mixer.init()
pygame.mixer.music.set_volume(20)
pygame.mixer.music.load("C:/oldof/button3.wav")

pygame.mixer.music.play()

#keys = pygame.key.get_pressed()
#keys = pygame.key.name()
#if event.key == K_CAPSLOCK:
 #   print("CAPS")

work = True
print("running...")
hellcount=0
speak = wincl.Dispatch("SAPI.SpVoice")


#if key[K_CAPSLOCK]: 
 #   print ("CAPSLOCK")

opts = { #useless now :(
    "konnor": ('коннор','Коннор',"Konnor","конор","коно","Коно","Конар","конар"),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси'),
    "cmds": {
        "ctime": ('текущее время','сейчас времени','который час'),
        "stupid1": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты')
    }
}

def stopwrk():
    work = False

def speak(what):
    print( what )
    speak.Speak(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower() #recognition
        print("[log] Распознано: " + voice) #LOG#
        cmd = voice
        #execute_cmd(cmd)
    
        if voice.startswith(opts["konnor"]):#Check for excepion
            #Obrashenie 
            #cmd = voice

            for x in opts['konnor']:
                cmd = cmd.replace(x, "").strip()
            
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
            #cmd = recognize_cmd(cmd)
            #cmd = input("text - ")
            #execute_cmd(cmd['cmd'])
            #cmd = voice
        #run
        execute_cmd(cmd)

    except sr.UnknownValueError: #check for errors
        print("[log] Голос не распознан!")
        #cmd = input("text - ")
        #execute_cmd(cmd)
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")
        cmd = input("text - ")

def recognize_cmd(cmd): # not using now
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC

def execute_cmd(cmd): #MAIN executions
    speak=wincl.Dispatch("SAPI.SpVoice")
    global hellcount


  
    if ('шутка' in cmd) or ("пошути"in cmd):
        # joke
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak("Мой пин-код это последние 4 цифры числа ПИ!")

    elif (cmd == "молчать") or (cmd == "тишина"):
    	exit()
        #quit()

    elif cmd == "открой блокнот" :
    	speak.Speak("Открываю")
    	os.system("C:/oldof/oldtxt.py")
    	os.system("C:/oldof/voice.py")

    elif ("запиши" in cmd):
    	cmd = cmd.replace("запиши","")
    	enter_note(cmd)

    elif ("вконтакте" in cmd):
        os.system("start http://vk.com/im")
        print("VK")

    elif (cmd == "выключение") or (cmd == "пока"):
        speak.Speak("Пока")
        pygame.mixer.music.load("C:/oldof/button2.wav")
        pygame.mixer.music.play()
        print("Stoped")
        work = False
        stopwrk()
        sys.exit()
        quit()

    elif ( cmd == "включи мою музыку" ) or ("музыка" in cmd):
        speak.Speak("Включаю")
        os.system("C:/oldof/OldMuz.py")
        os.system("C:/oldof/voice.py")

    elif ("переведи" in cmd ):
        transl=cmd.replace("переведи","")
        os.system("start https://translate.yandex.ru/?text="+transl)

    elif ("привет" in cmd) or ("приветствую" in cmd) or ("hello" in cmd):
    	#speak = wincl.Dispatch("SAPI.SpVoice")
    	hellcount+=1
    	if hellcount == 5 or hellcount == 10:
    		speak.Speak("Уже здаровались")

    	hellor = ["приветствую","Hello world!","привет","И снова дратути"]
    	speak.Speak(random.choice(hellor))

    elif ('который час' in cmd) or ('сколько времени' in cmd) or ('время' in cmd): #ERROR IS HERE
        # time
        now = datetime.datetime.now()
        #speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak("Сейчас " + str(now.hour) + "часов"+":" + str(now.minute)+"минут")
        print("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif ('погода' in cmd):
        weth = weather.get()
        speak.Speak('На улице '+ weth + 'градусов' )

    elif ('скачать музыку' in cmd):
        print("kissvk.com")
        speak.Speak('Открываю браузер!!!')
        os.system('start http://kissvk.com')

    elif ('что такое' in cmd):
        search = cmd.replace("что такое ","")
        os.system("start http://yandex.ru/search/?text="+search)
        speak.Speak("Нашел это в интернете")

    elif ("спасибо" in cmd) or ("благодарю" in cmd):
        speak.Speak("пожалуйста!")
        print(";)")

    elif ("заблокируй" in cmd) or ("блокировка" in cmd):
        pyautogui.press(['winleft','l'])
        speak.Speak('Ваш компьютер заблокирован')
        now = datetime.datetime.now()
        print('Заблокировано в '+ str(now.hour)+':'+str(now.minute))

    elif ("скриншот" in cmd):
        pyautogui.press('printscreen')
        pygame.mixer.music.load("C:/oldof/button9.wav")
        pygame.mixer.music.play()
        #speak.Speak("Скрин")
        print("scrsht")

    elif ('пауза' in cmd) or ("стоп" in cmd):
        stopsong()

    elif ('тише' in cmd) or ('потише' in cmd):
        print("-")
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')


    elif ('громче' in cmd) or ('погромче' in cmd):
        print("+")
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')

    elif ("полная тишина" in cmd):
        pyautogui.press('volumemute')



    
    else:
        print('Команда не распознана, повторите!')

def enter_note(cmd):
	file1 = open("C:/oldof/noter/temp.tx","w+")
	file1.write(cmd)
	file1.close()
	#import oldtxt
	#import voice
	#subprocess.Popen([sys.executable, "txt", cmd])
	os.system("C:/oldof/oldtxt.py")
	os.system("C:/oldof/voice.py")	


#def getusername():
 #   callback()
  #  filename = open("C:/oldof/usrname.txt","w")
   # filename.write(cmd)
    #filename.close() GET USER NAME BY VOICE AND ASKING 





# starting
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)

with m as source:
    r.adjust_for_ambient_noise(source)

#speak_engine = pyttsx3.init()
#voices = speak_engine.getProperty('voices')
#speak_engine.setProperty('voice', voices[1].id)
#speak.Speak("Работаю")
if os.path.exists("C:/oldof/noter/temp.tx"):
	os.remove("C:/oldof/noter/temp.tx")
speak = wincl.Dispatch("SAPI.SpVoice")

#speak.Speak("Slushayu.")

if os.path.exists("C:/oldof/usrname.txt"):
    file = open("C:/oldof/usrname.txt","r")
    name = file.read()
    speak.Speak("Привет, "+name)
else:
    speak.Speak("Slushayu!")
   # speak.Speak("Как мне вас называть?")
 #   getusername()

#work=True
print("Listen...\n")

stop_listening = r.listen_in_background(m, callback)
while work == True: time.sleep(0.1) # infinity 