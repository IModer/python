import keyboard as kb
import os
from tkinter import Tk
import datetime as dt
import time
import os
import subprocess

today = dt.datetime.now()
r = Tk()
r.withdraw()
path = "C:\\Users\\theco\\Desktop\\archive.txt"
data = ""
while kb.is_pressed('alt+c') == False:
	if kb.is_pressed('alt+a'):
		n = 40
		data = ""
		raw = r.clipboard_get()
		rawstr = str(raw)
		#print(rawstr[1])
		file = open(path, "a")
		file.write("\n<<<<<<<<" + today.strftime("%x") + ">  :  <" + today.strftime("%X") + ">>>>>>>>")
		for x in range(len(rawstr)):
			if (x % n+2) > n:
				data = data + "\n"
			data = data + rawstr[x]
			#print(data)
		file.write("\n" + data)
		for x in range(5):
			file.write("\n")
		time.sleep(0.5)
		file.close()
		#print(data)
		#r.clipboard_clear()
		
	if kb.is_pressed('alt+q'):
		subprocess.Popen(r'explorer /select,"G:\\Anime"')
		os.startfile('C:\\Users\\theco\\Desktop\\anime.txt')
		time.sleep(0.5)

	if kb.is_pressed('alt+u'):
		show = input('') 
		ep = input('')
		mypath_half = '"G:\\Anime\\' + show + '"'
		mypath = 'explorer /select,' + mypath_half
		subprocess.Popen(r + mypath)
exit()
