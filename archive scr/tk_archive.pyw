import keyboard as kb
import os
from os import listdir
from os.path import isfile, join, isdir
import tkinter as tk
import tkinter.scrolledtext as tkst
import datetime as dt
import time
import subprocess

today = dt.datetime.now()
#tk.Tk.withdraw()

def run_my_video():
			#showi = input('')
			show = e1.get() 
			#carep = input('')
			carep = e2.get()
			#mypath = 'r\'explorer /select,\"G:\\Anime\\{}\\{}\"\''
			#subprocess.Popen(mypath.format(show, ep))

			mypath = 'G:\\Anime\\{}\\{}'
			mydir = 'G:\\Anime\\{}'
			mydirformat = mydir.format(show)
			#print(str(mydir.format(show)))
			try:
				onlyfiles = [f for f in listdir(str(mydirformat)) if isfile(join(str(mydirformat), f))]
			except:
				v1.set("Unexpected error, the folder doesn't exists")
			
			#print(onlyfiles)
			try:
				currentep = onlyfiles[int(carep)-1]
			except :
				v2.set("Unexpected error, this episode doesn't exists")
			os.startfile(str(mypath.format(show, currentep)))
			master.destroy()
path = ""
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
		#subprocess.Popen(r'explorer /select,"G:\\Anime"')
		os.startfile('')
		time.sleep(0.5)

	if kb.is_pressed('alt+u'):
		master = tk.Tk()

		master.title("Anime")
		master.geometry("450x135")
		e1 = tk.Entry(master)
		e2 = tk.Entry(master)
		e1.grid(row=0, column=1)
		e2.grid(row=1, column=1)
		v1 = tk.StringVar()
		v2 = tk.StringVar()
		tk.Label(master, textvariable=v1).grid(row=0, column=2)
		tk.Label(master, textvariable=v2).grid(row=1, column=2)
		tk.Button(master, text='Indítás', command=run_my_video, height=5, width=10).grid(row=3, column=1, sticky=tk.W)
		tk.Button(master, text='exit', command=master.destroy, height=5, width=10).grid(row=3, column=3, sticky=tk.W)

		#onlydir = [f for f in listdir("G:Anime\\") if isdir(join("G:Anime\\", f))]
		#print(onlydir)
		#my_lable_text = ""
		#for x in onlydir:
		#	my_lable_text += x + "\n"


		#text = tk.Text(master)
		#text.insert('1.0', my_lable_text)
		#scroll_y = tk.Scrollbar(master, orient="vertical", command=text.yview)
		#text.configure(yscrollcommand=scroll_y.set)
		#text.pack()
		#print(my_lable_text)
		#tkst.Scrolledtext(master, wrap=tl.WORD, width=20, height=10)
		#editArea.insert(tk.INSERT,my_lable_text)
		#tk.Label(master, text=my_lable_text, justify="left").grid(row=0, column=3)

		master.mainloop()
exit()
