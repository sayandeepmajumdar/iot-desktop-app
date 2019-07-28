import tkinter
import tkinter.messagebox as tkMessageBox
import sys
import os
import shutil
from serial import *
import requests
from pyfirmata import Arduino, util
import time

root = tkinter.Tk()
root.title('TAL-IoT (Budding Innovator v3.0)')
root.resizable(width=True, height=False)

# Code to add widgets will go here...
C = tkinter.Canvas(root, bg="#212121", height=300, width=400)
C.grid(row=2,column=2)
board = Arduino("COM4")
# ser = Serial("COM4", baudrate = 9600, timeout=1)
tkinter.Label(root, text='Remote For Light',bg="#e64a19").grid(row=2,column=2,sticky='N',pady='10')

def lightoff():
   
   tkMessageBox.showinfo( "TAL-IoT (Budding Innovator v3.0)", "Light OFF")
   arduinoData = 0
   # print("Data:", arduinoData)
   URL = "https://api.thingspeak.com/update?api_key=<Your_API_KEY>"
   PARAMS = { 'field1' : arduinoData }
   requests.get(url=URL,params=PARAMS)
   dataToArduino()

def lighton():
   # ser = Serial("COM4", baudrate = 9600, timeout=1)
   tkMessageBox.showinfo( "TAL-IoT (Budding Innovator v3.0)", "Light ON")
   arduinoData = 1
   # print("Data:", arduinoData)
   URL1 = "https://api.thingspeak.com/update?api_key=<Your_API_KEY>"
   PARAMS1 = { 'field1' : arduinoData }
   requests.get(url=URL1,params=PARAMS1)
   dataToArduino()

def dataToArduino():
   
   # while 1:
   URL2 = "https://api.thingspeak.com/channels/834537/fields/1.json?api_key=<Your_API_KEY>"

   PARAMS2 = { 'results' : 2 }

   res = requests.get(url=URL2,params=PARAMS2)
   # print(res.content) #getting value in List and json format
   resjson = res.json()
   feed = resjson['feeds']
   val = feed[1]['field1']
   print("Data:", val)
   board.digital[12].write(int(val))
   # time.sleep(0.2)
   # board.digital[12].write(0)
   # time.sleep(0.2)








on = tkinter.Button(root,bg="#43a047", text ="On", command = lighton).grid(row=2,column=2,sticky='NW',pady='90',padx="90")

off = tkinter.Button(root,bg="#ffee58", text ="Off", command = lightoff).grid(row=2,column=2,sticky='NE',pady='90',padx="90")


root.mainloop()